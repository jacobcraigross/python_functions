# print formatting %s' %(x) <--- inserting into a string

def greeting(name):
    print 'Hello %s' %name

greeting('Jacob')

# Hello Jacob
#-------------------------------------------------------

# A simple addition function, followed by two prime number functions.

def addition(num1, num2):
    print num1 + num2

addition(34, 66)

# 100

def prime_checker(num):
    '''
    INPUT: a number
    OUTPUT: a print statement with the VERDICT!
    '''
    for i in range(2, num):
        if num % i == 0:
            print 'not prime'
            break
    else: # if never mod 0, then prime
        print 'prime'

prime_checker(23)
prime_checker(14)
prime_checker(11)

# prime
# not prime
# prime


# slightly upgraded way to check primes.

import math

def prime_check(num):
    '''
    A better way to check for primes.
    '''
    if num % 2 == 0 and num > 2:
        return False
    for n in range(3, int(math.sqrt(num)) + 1, 2):
        if num % n == 0:
            return False
    return True

print prime_check(22)
print prime_check(7)

# False
# True
