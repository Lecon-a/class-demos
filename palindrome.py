gt = 0
grt = []

for i in range(100, 1000):
    for j in range(100, 1000):
        palin = str(i * j)
        if len(palin) > 5 and int(palin[0]) == int(palin[-1]):
            if gt < int(palin[0]) and int(palin[1]) == int(palin[-2]):
                gt = int(palin[0])
                grt.append(int(palin))

print("The Largest Palindrome is : {0}".format(max(grt)))