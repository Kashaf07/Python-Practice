# Sample tuple with random integers
random_tuple = (12, 7, 45, 22, 65, 80, 3, 18, 88, 5)

even_count = 0
odd_count = 0

for num in random_tuple:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"The tuple is: {random_tuple}")
print(f"Count of even numbers: {even_count}")
print(f"Count of odd numbers: {odd_count}")
