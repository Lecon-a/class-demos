sumOfFirstHundred = 0
sumOfSquareOfFirstHundred = 0

for i in range(1, 101):
    sumOfSquareOfFirstHundred += (i**2)
    sumOfFirstHundred += i

squareOfSumOfFirstHundred = sumOfFirstHundred ** 2

difference = squareOfSumOfFirstHundred - sumOfSquareOfFirstHundred  

print(difference)