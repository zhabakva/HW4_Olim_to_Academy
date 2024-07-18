def ways_to_step(n):
    if n == 0: return 1
    if n == 1: return 1
    elif n == 2: return 2
    else:
        return ways_to_step(n-1)+ways_to_step(n-2)


while True:
    try:
        num1 = int(input("Enter the number of steps: "))
        break
    except ValueError:
        print("Wrong Format. Please enter an integer.")
if num1 < 0:
    print("Error. You have to enter a positive integer.")
else:
    print(ways_to_step(num1))


