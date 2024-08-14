

    # So here we can use formatting
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"


print(f"{BOLD}{GREEN}My First Pyhton Project{RESET}")

print(f"{RED}First Method{RESET}")

num1 = int(input("Please enter First number: "))
opreator = input("Please enter operator: ")
num2 = int(input("Please enter Second number: "))
if opreator == "+":
  print(f"Your answer is = {UNDERLINE}{num1 + num2} {RESET}")
elif opreator == "-":
  print(f"Your answer is = {UNDERLINE}{num1 - num2} {RESET}")
elif opreator == "*":
  print(f"Your answer is = {UNDERLINE}{num1 * num2} {RESET}")
elif opreator == "/":
  print(f"Your answer is = {UNDERLINE}{num1 / num2} {RESET}")


print(f"{RED}Second Method{RESET}")

user_input = input("Please enter Expression: ")

operators = ['+', '-', '*', '/']

operator = ""
num1 = ""
num2 = ""

for i in range(len(user_input)):
  if user_input[i].isdigit() and not operator:
    num1 += user_input[i]
  elif user_input[i] in operators:
    operator = user_input[i]
  else :
    num2 += user_input[i]

num1 = int(num1)
num2 = int(num2)


if opreator == "+":
  print(f"Your answer is = {UNDERLINE}{num1 + num2} {RESET}")
elif opreator == "-":
  print(f"Your answer is = {UNDERLINE}{num1 - num2} {RESET}")
elif opreator == "*":
  print(f"Your answer is = {UNDERLINE}{num1 * num2} {RESET}")
elif opreator == "/":
  print(f"Your answer is = {UNDERLINE}{num1 / num2} {RESET}")
else :
  print("Invalid expression Give in this form (a + b)" )