# Heath Hilton
# 11/06/2022

# Program: 4.2 - Small & Green

# The program is using very basic characteristics to figure out which item the user has.

small = True
green = True

print("You say that your item is small and green, let's see if we can figure out what it is.")

if small == True:
    if green == True:
        print("Your small and green item is a pea.")
    else:
        print("Your small and not green item is a cherry.")
else:
    if green == True:
        print("Your large and green item is a watermelon.")
    else:
        print("Your large and not green item is a pumpkin.")
