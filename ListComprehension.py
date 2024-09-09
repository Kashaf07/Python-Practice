squares=[(x,x**2) for x in [1,2,3]]
print(squares)
pairs=[(x,y) for x in [1,2,3] for y in['a','b']]
print(pairs)
v=[1,2,3]
points=[(x,y) for x in v for y in v]
print(points)