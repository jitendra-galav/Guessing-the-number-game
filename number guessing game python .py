import random
cnumber=random.randrange(1,101) # 1(include) and 101 (not include)
userinput=int(input("enter your number..."))
if userinput > cnumber:
   print("computer number",cnumber)
   print("your guess number is too high")
elif userinput < cnumber:
   print("compuer number",cnumber)
   print("your guess number is too low")
else:
    print("computer number",cnumber)
    print("your guess number is equall ")









