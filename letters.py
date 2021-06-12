import random, string

my_list = []

# FUNCTIONS
for x in range(5):
    my_letter = random.choice(string.ascii_uppercase)
    letter = random.choice(my_letter)
    my_list.append(my_letter)

    if x not in my_list:
        my_list.append(x)
    else:
        x = x-1

for y in range(6):
    x = random.choice(string.ascii_uppercase)
    if x not in my_list:
        my_list.append(x)
    else:
        y = y-1

print(my_list)
