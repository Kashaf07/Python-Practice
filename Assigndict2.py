A = {20, 19, 2, 10, 7} 
B = {4, 10, 5, 6, 9, 7} 
C = {10, 19}
print(A) #{2, 19, 20, 7, 10}
print(20 in A) #True
print(20 not in A) #False
print(A & B) #{10, 7}
print(A|B) #{2, 4, 5, 6, 7, 9, 10, 19, 20}
print(C<A) #True
print(C<=A) #True
print(C<=B) #False
print(A<=A) #True
print(A<A) #False
print(len(A)) #5
print({x + 2 for x in range(10)})  #{2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print({x - 2 for x in A}) #{0, 5, 8, 17, 18}
print({x - 2 for x in A if x < 10}) #{0, 5}