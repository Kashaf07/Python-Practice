def maxThree(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))
m = maxThree(n1, n2, n3)
print('Maximum of three numbers is:', m)
