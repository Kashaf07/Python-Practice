user_input = input("Enter a string: ")
total_characters = len(user_input)
string_repeated = user_input * 10
first_character = user_input[0]
first_three_characters = user_input[:3]
last_three_characters = user_input[-3:]
string_backwards = user_input[::-1]
seventh_character = user_input[6] if total_characters >= 7 else "String is too short"
without_first_and_last = user_input[1:-1]
string_in_caps = user_input.upper()
string_replaced = user_input.replace('a', 'e')

# Print the results
print(f"(a) Total number of characters: {total_characters}")
print(f"(b) String repeated 10 times: {string_repeated}")
print(f"(c) First character: {first_character}")
print(f"(d) First three characters: {first_three_characters}")
print(f"(e) Last three characters: {last_three_characters}")
print(f"(f) String backwards: {string_backwards}")
print(f"(g) Seventh character: {seventh_character}")
print(f"(h) Without first and last characters: {without_first_and_last}")
print(f"(i) String in all caps: {string_in_caps}")
print(f"(j) 'a' replaced with 'e': {string_replaced}")
