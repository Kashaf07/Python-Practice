# Create a dictionary representing the database
d = {
        "name": "Router1",
        "IP": "1.1.1.1",
        "username": "zframez",
        "pwd": "zframez"
    }

for z in d.keys():
    print(z)

given_key = input("Enter a key: ")
if given_key in d:
    value = d[given_key]
    print(f"The value for key '{given_key}' is {value}.")
else:
    print(f"The key '{given_key}' does not exist in the database.")

new_value = {
        "name": given_key,
        "IP": "New IP",
        "username": "New User",
        "pwd": "New Password"
    }
d[given_key] = new_value
print(f"The key '{given_key}' has been added to the database with the value {new_value}.")

print("Updated Database:")
for key, value in d.items():
    print(key, ":", value)





