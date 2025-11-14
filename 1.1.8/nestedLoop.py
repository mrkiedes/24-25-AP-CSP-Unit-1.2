num1 = 6
num2 = 7

# Nested Loop Example
for n in range(num1):
    #print("N: " + str(n))
    for o in range(num2):
        #print("O: " + str(o))
        if n > o:
            print("n was bigger!")
        elif n < o:
            print("o was bigger!")
        else:
            print("They were equal!!!")