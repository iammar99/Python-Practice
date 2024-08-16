
"""
Write a program that take input from the user and tells whether number is even or odd and is it a prime number or not
"""

# Color Defining

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"


check = False
prime = False

def checkInput(number):
    for i in range(len(number)):
        if number[i].isalpha():
            print(RED + "Invalid Input! Please enter a number." + RESET)
            return False
    return True
            
while not check:
    num = input("Enter any number :-")
    check = checkInput(num)        
    
num = int(num)

for i in range(2,num // 2):
    if num % i == 0:
        prime = True
        break
    else:
        prime = False
   
   

if num % 2 == 0 and prime == True:
    print(f"{GREEN}The Number is Even and It is also a prime number{RESET}")
elif num % 2 != 0 and prime == True:
    print(f"{GREEN}The Number is Odd and It is also a prime number{RESET}")
elif num % 2 == 0 and prime == False:
    print(f"{GREEN}The Number is Even But it is not a prime number{RESET}")
else :
    print(f"{GREEN}The Number is Odd But it is not a prime number{RESET}")