num1 =input("type first number: ")
num1 = int(num1)
ops = ["1: Add","2: Subtract", "3: Multiple", "4: Divide"]
for op in ops:
    print(op)
chose = input()
chose = int(chose)
num2 =input("type second number: ")
num2 = int(num2)
if chose == 1:
    print(num1 + num2)
elif chose == 2:
    print(num1 - num2)
elif chose == 3:
    print(num1 *num2)
elif chose == 4:
    print(num1 / num2)
else: 
    print( "please choose one of the 4 numbers")
