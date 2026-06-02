print("welcome to calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("enter your choice: "))

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if choice == 1:
    print("result:",num1 + num2)
elif choice == 2:
    print("result:",num1 - num2)
elif choice == 3:
    print("result:",num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("result:",num1 / num2)
    else:
        print("cannot divide by zero")
else:
    print("invalid choice")

