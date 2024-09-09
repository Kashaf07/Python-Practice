def Area_rect(length,breadth):
    a=length*breadth
    return a

def Peri_rect(lent,bred):
    b=2*(lent+bred)
    return b

l=int(input('Enter length of rectangele:'))
b=int(input('Enter breadth of rectangele:'))
print('The area of Rectangle is:',Area_rect(l,b))
print('The perimeter of Rectangle is:',Peri_rect(l,b))