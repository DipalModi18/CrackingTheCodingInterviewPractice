# Solution 1
test_str = "testuniquechars"
has_unique = True
list_char = []
for char in test_str:
    if char in list_char:
        print("String does not have unique characters")
        has_unique = False
        break
    else:
        list_char.append(char)

# Solution 2
array = set(test_str)
if len(array) == len(test_str):
    print("String has all unique characters")
else:
    print("String does not have unique characters")
