"""
*
**
***
****
*****
"""
# input 5
user_input = int(input("Enter Number: "))
for row in range(user_input+1):
    for coloumn in range(row):
        print("*",end="")
    print()