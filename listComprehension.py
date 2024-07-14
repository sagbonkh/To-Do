# # This shows the best times to use list comprehension

# names = ["john smith", "jay santi", "eva kuki"]

# names = [name.title() for name in names]

# print(names)

# # shows how to replace text in a list of strings
# filenames = ["1.doc","1.report", "1.presentation"]

# filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

# print(filenames)

# # show how to count the characters for each string in a list of strings
# usernames = ["john 1990", "alberta1970", "magnola2000"]

# characters = [len(username) for username in usernames]

# print(characters)

# # converts string nums to floating points
# user_entries = ['10', '19.1', '20']

# float_enteries = [float(nums) for nums in user_entries]

# print(float_enteries)

user_entries = ['10', '19.1', '20']

num = 0
num = [num + float(entry) for entry in user_entries]
print(num)