done = False
n, m = 0, 100
while not done and n != m:
    n = int(input('Enter:'))
    if n < 0:
        break
    print("n =", n)
