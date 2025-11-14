num1 = 6
num2 = 6
# Header: if booleanStatement:
if num1 > num2:
    # Body: holds the statements to execute
    # Everything in the same tab level is in the body
    print("Num1 is bigger")
# Elif: Stands for else if.  Check the first condition, then check
# them in the order shown.
elif num2 > num1:
    print("Num 2 is bigger")
else:
    print("Num1 is equal to Num2")