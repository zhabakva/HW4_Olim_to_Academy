def algE(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    if a>b:
        return algE(b, a % b)
    else:
        return algE(a, b % a)


while True:
    try:
        num1 = int(input("Enter the first integer: "))
        break
    except ValueError:
        print("Wrong Format. Please enter an integer.")

while True:
    try:
        num2 = int(input("Enter the second integer: "))
        break
    except ValueError:
        print("Wrong Format. Please enter an integer.")
print(algE(num1, num2))
