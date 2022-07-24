prod = 1
count = 0

for i in range(3628800, 1000000000):
    for j in range(1, 21):
        if i % j == 0:
            count += 1
            if count == 20:
                print(i)
                break #when found
        else:
            count = 0   
    count = 0