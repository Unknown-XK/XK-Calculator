#XK-Calculator
#Made by Unknown-XK

print("Hello to Calculator v1.0.1")
print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")
print("5- Power of two")
print("6- Exit")
x = int(input("Enter your choice: "))
if (x >= 1 and x <=4):
  print("Enter two numbers: ")
  num1 = int(input())
  num2 = int(input())
  if choice == 1:
    res = num1 + num2;
    print("Result = ", res)
  elif choice == 2:
    res = num1 - num2
    print("Result = ", res)
  elif choice == 3:
    res = num1 * num2
    print("Result = ", res)
  else:
    res = num1 / num2;
    print("Result = ", res)
elif x == 5:
  print("Enter a number:")
  num = int(input())
  pwr = pow(num, 2)
  print("result =", pwr)
elif x == 6:
    exit()
else:
    print("Input error!")
if (x >= 1 and x <= 5):
  print("Thank you")
elif x == 6:
  print("Good bye.")
else:
  print("Please correct the input.")
