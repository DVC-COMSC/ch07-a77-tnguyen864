
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

num3 = []

if len(num1) < len(num2):
    for i in range(len(num1)):
        num3.append(num1[i])
        num3.append(num2[i])
    x = len(num2) - len(num1)
    for i in range(x):
        num3.append(num2[i-1])

if len(num1) > len(num2):
    for i in range(len(num2)):
        num3.append(num1[i])
        num3.append(num2[i])
    x = len(num1) - len(num2)
    for i in range(x):
        num3.append(num1[i-1])
print(num3)