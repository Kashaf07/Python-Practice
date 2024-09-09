def maxTwo(x,y):
    if x>y:
        return x
    else:
        return y
    
n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
m=maxTwo(n1,n2)
print('Maximum of two number is:',m)