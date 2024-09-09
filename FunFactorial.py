def factI(n):
    result=1
    while n>1:
        result=result*n
        n=n-1
    return result
num=int(input('Enter an integer:'))
print('The factorial of',num,'is',factI(num))