"""Ally Smith"""


def main():
    # User to Input Name
    name, valid_entry = get_name()# Print every second letter in the name
    if valid_entry is True:
        char_print(name)


def char_print(name):
    frequency = int(input("Print every _ letter "))
    for char in name[::frequency]:
        print(char)


def get_name():
    name = input("Enter Your Name: ")
    # Check the Input isn't Blank
    valid_entry = False
    while not valid_entry:
        try:
            if len(name) != 0:
                valid_entry = True
        except:
            print("Invalid Input. Please try again.")

    return name, valid_entry


main()

