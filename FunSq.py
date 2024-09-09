def Area_sq(side):
    a=side*side
    return a

def Peri_sq(s):
    b=4*s
    return b

sides=int(input('Enter side of square:'))
print('The area of Square is:',Area_sq(sides))
print('The perimeter of Square is:',Peri_sq(sides))