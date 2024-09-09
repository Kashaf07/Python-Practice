def factR(n):
    if n==1:
        return n
    else:
        return n*factR(n-1)

num=int(input('Enter a number'))
print('The factorial of',num,'by recursion is',factR(num))