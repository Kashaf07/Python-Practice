# Create a string called "something" with the value "Completely Different"
something = "Completely Different"

# Print all the properties and methods of the string
print(dir(something))

# Use a string method to count the number of times the character "t" is present in the string
count_t = something.count("t")
print(f"The character 't' appears {count_t} times in the string.")

# Use a string method to find the first position of the sub-string "plete" in the string
position_plete = something.find("plete")
print(f"The sub-string 'plete' starts at position {position_plete} in the string.")

# Use a string method to split the string by the character "e"
split_by_e = something.split("e")
print("String split by 'e':", split_by_e)

# Create a new string ("thing2") that replaces the word "Different" with "Silly"
thing2 = something.replace("Different", "Silly")
print("Updated string 'thing2':", thing2)

# Try to assign the letter "B" to the first character of the string "something"
# This will cause an error because strings are immutable, and you cannot change individual characters this way.
# You would need to create a new string with the desired modification.
# Uncomment the following line to see the error.
# something[0] = "B"
