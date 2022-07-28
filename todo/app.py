from flask import Flask, render_template, redirect, url_for, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import sys

import dsn

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dsn.URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class TaskList(db.Model):
    __tablename__='tasklists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)

    def __repr__(self):
        return f"<TaskList :: ID => {self.id}, name => {self.name}>"

class Todo(db.Model):
    __tablename__='todos'
    date = datetime.now()
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    createdTime = db.Column(db.String(), nullable=False, default=str(date))
    tasklist_id = db.Column(db.Integer, db.ForeignKey('tasklists.id'), cascaded, nullable=False)

    def __repr__(self):
        return f"<TODO :: ID => {self.id}, desc => {self.description}, Created Time => {self.createdTime}, Completed => {self.completed}>"

@app.route("/")
def index():
    return redirect(url_for('get_task_list', tasklist_id=1))

@app.route("/todo/<tasklist_id>")
def get_task_list(tasklist_id):
    return render_template('index.html',
        lists = TaskList.query.all(),
        active_list = TaskList.query.get(tasklist_id),
        tasks = Todo.query.filter_by(tasklist_id=tasklist_id).order_by('id').all()
        )

@app.route("/todo/<list_id>/create_task", methods=['POST'])
def create_task(list_id):
    error = False
    try:
        body = {}
        new_task = request.get_json()['description']
        # print('==============><================')
        todo = Todo(description=new_task, tasklist_id=list_id)
        db.session.add(todo) 
        db.session.commit()  
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:   
        db.session.close()
    if not error:
        return jsonify(body)
    else:
        abort(400)    

@app.route('/todo/<task_id>/set_completed', methods=['POST'])
def set_completed(task_id):
    try:
        newTaskCompleted = request.get_json()['taskCompleted']
        todo = Todo.query.get(task_id)
        todo.completed = newTaskCompleted
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))             

@app.route('/todo/<active_list_id>/rename_list', methods=['POST'])
def rename_list(active_list_id):
    try:
        newName = request.get_json()['newName']
        taskList = TaskList.query.get(active_list_id)
        taskList.name = newName
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index')) 

@app.route('/todo/<task_id>/delete_task', methods=['POST'])
def delete_task(task_id):
    # print("=====> ", task_id)
    try:
        todo = Todo.query.get(task_id)
        db.session.delete(todo)
        # or Todo.query.filter_by(id='value').delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))            

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0')