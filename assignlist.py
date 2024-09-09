lst = [20, 1, -34, 40, -8, 60, 1, 3]
print(lst)  #[20, 1, -34, 40, -8, 60, 1, 3]
print(lst[0:3]) #[20, 1, -34]
print(lst[4:8]) #[-8, 60, 1, 3]
print(lst[4:33]) #[-8, 60, 1, 3]
print(lst[-5:-3]) #[40, -8]
print(lst[-22:3]) #[20, 1, -34]
print(lst[4:]) #[-8, 60, 1, 3]
print(lst[:]) #[20, 1, -34, 40, -8, 60, 1, 3]
print(lst[:4]) #[20, 1, -34, 40]
print(lst[1:5]) #[1, -34, 40, -8]
print(-34 in lst) #True
print(-34 not in lst) #False
print(len(lst)) #8