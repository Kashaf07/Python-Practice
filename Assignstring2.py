s = "I love to write python"
split_s = s.split()
# print(split_s)  ['I', 'love', 'to', 'write', 'python']
for word in split_s:
    if 'i' in word:
        print(f"I found 'i' in: '{word}'")