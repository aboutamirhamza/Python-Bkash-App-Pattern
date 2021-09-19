"""
1
12
123
1234
12345
"""
# input 5
user_input = int(input("Enter Number: "))
for row in range(user_input+1):
    for col in range(1,row):
        print(col,end="")
    print()