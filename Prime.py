n=int(input('Enter a number to find if it is prime:'))
prime=1
for factor in range(2,n):
    if n % factor == 0:
        prime=0
if prime==1:
    print(n,'is prime!') 
else:
    print(n,'is not prime!')