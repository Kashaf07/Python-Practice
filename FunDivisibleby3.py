def divisible(number):
    return number % 3 == 0

# function use
num = int(input('Enter a Number:'))
result = divisible(num)
if result:
    print(num,"is divisible by 3.")
else:
    print(num,"is not divisible by 3.")