s = "I like Ice-cream. Jack is learning python.  This is challenge number 1."
l = list(s)

for index, char in enumerate(l):
    print(f'Character at index {index} is {char}')

d = dict()

for c in l:
    # If key doesn't exist, it will be created with value 0, then incremented
    d[c] = d.get(c, 0) + 1

print("\nCharacter counts:")
for char, count in d.items():
    print(f"{char}: {count}")