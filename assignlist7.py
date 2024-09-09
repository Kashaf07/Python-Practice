#[1, 4, 9, 16, 25]
print([x**2 for x in range(1, 6)])
#[0.25, 0.5, 0.75, 1.0, 1.25. 1.5]
print([0.25 * x for x in range(1, 7)])
#[('a', 0), ('a', 1), ('a', 2), ('b', 0), ('b', 1), ('b', 2)]
print([(a, b) for a in ['a', 'b'] for b in range(3)])
