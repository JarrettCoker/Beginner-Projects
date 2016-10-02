# What's My Number?
# Python 3.5.10
# Written by rsz

number = ''
k = ''

def check_dig(i): #checks if number contains 1 or 7
    num = str(i)
    l = len(num)
    for j in range(0,l):
        e = num[j]
        if int(e) == 1 or int(e) == 7:
            return False
            break
        else:
            return True
        
def is_prime(a): #returns True for a prime number
    if a >= 2:
        for p in range(2,a):
            if (a % p) == 0:
                return False
        else:
            return True

def dig_sum(i): #returns sum of digits
    return (sum(int(x) for x in str(i)))


for i in range(1,1001):
    if len(str(i)) >= 2: 
        if is_prime(i):
            if check_dig(i):
                suM = dig_sum(i)
                if suM <= 10:
                    k = str(i)
                    ls = (int(k[0]) + int(k[1])) # sum of first two digits
                    if (ls % 2 ) != 0: 
                        q = str(i)
                        #second to last digit even. returns zero, so zero omitted
                        if (int(q[len(q)-2]) % 2) == 0 and int(q[len(q)-2]) != 0:
                            # last digit equals to no of digits
                            if int(q[len(q)-1]) == int(len(str(i))):
                                print(i)

    else:
        continue
                    
                
        
