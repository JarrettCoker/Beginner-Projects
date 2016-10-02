# Multiplication Table
# Python 3.5.10
# Written by rsz

def multiply(lhs):
    for i in range(1,9):
        print(lhs, " x ", i, " = " ,lhs * i)
        
        
lhs = 1     
while lhs <=9:
    multiply(lhs)
    lhs += 1
    print(' ' * 5)


