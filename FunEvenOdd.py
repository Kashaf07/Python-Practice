def EvenOdd(n):
    if n % 2 == 0 :
        return True
    else:
        return False
# Use of function
Num = int(input('Enter an integer : '))
if EvenOdd(Num) :
    print(Num, ' is an even ! ')
else :
    print(Num, ' is an odd ! ')