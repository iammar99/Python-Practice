
"""
Write a program that calculates the sum of the following series using function. The main() function inputs a number and passes it to a function. The function finds the sum from 1 to the given number and returns the result to main() function.
1+1/11+1/2+1/3+1/4!...........
"""

# Color Defining

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"

print(f"{RED}--------------- Program To find Below Series --------------- {RESET}")
print(f"{GREEN}--------[1+1/11+1/2+1/3+1/4!...........]--------{RESET}")

num = input("Enter number :- ")

while num.isalpha():
  num = input("Please Enter a number :- ")

num = int(num)
def factorial(n):
  ans = 1
  for i in range(n):
    ans *= n
  return ans 
sum = 0 


for i in range(num):
  sum += 1 / factorial(num)
  print(1 , "/"  ,  sum)

print(f"{GREEN}The answer of your Fabiconni series is :- {RESET}" , sum)


  
