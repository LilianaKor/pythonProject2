# # Created sheet
# sheet = ['apple', 12, 5.6, 'Banana', 'Apricot', 'Orange', False, 66, 1989, 'Pear', 'Avocado', 'grape', 'aston villa']
#
# # Required leaf - filtering strings starting with 'a' or 'A'
# required_leaf = [item for item in sheet if isinstance(item, str) and item.lower().startswith('a')]
#
# print(required_leaf)

# Created sheet
# my_sheet = ['apple', 12, 5.6, 'Banana', 'Apricot', 'Orange', False, 66, 1989, 'Pear', 'Avocado', 'grape', 'aston villa']

# Required leaf - filtering strings starting with 'a' or 'A'
# my_new = []
# for item in my_sheet:
#     if isinstance(item, str) and item[0].lower() == 'a':
#         my_new.append(item)
#
# print(my_new)

# item[0].lower() == 'a': Here, item[0] accesses the first character of the string stored in the variable item.
# Then, lower() is called on that character to convert it to lowercase. Finally, we check if the lowercase version
# of the first character is equal to the lowercase letter 'a'.
#
# my_new = []
# for item in my_sheet:
#     if type(item) == str and item[0].lower() == 'a':
#         my_new.append(item)
#
# print(my_new)
#
# # Created sheet
# sheet = ['apple', 12, 5.6, 'Banana', 'Apricot', 'Orange', False, 66, 1989, 'Pear', 'Avocado', 'grape', 'aston villa']
#
# # Required leaf - filtering strings starting with 'a' or 'A'
# required_leaf = []
#
# # Iterate through each item in the sheet
# for item in sheet:
#     # Check if the item is a string and starts with 'a' or 'A'
#     if isinstance(item, str) and (item.startswith('a') or item.startswith('A')):
#         # If so, add it to the required_leaf list
#         required_leaf.append(item)
#
# # Print the filtered list
# print(required_leaf)

fishes = ['Roan', 'Bass', 'Mako', 'Carp', 'Tuna', 'Dory', 'Snook', 'Perch', 'Manta', 'Koi', 'Goby', 'Smelt', 'Trout', 'Clown', 'Dotty', 'Guppy', 'Pike', 'Shark', 'Hake']
my_fish = [fish for fish in fishes if len(fish) >= 5]
friend_fish = [fish for fish in fishes if len(fish) < 5]

print("Мои рыбы:", my_fish)
print("Рыбы друга:", friend_fish)

