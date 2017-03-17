#Ascii Table

def main():
    #Constants
    LOWER = 33
    UPPER = 127

    print("Are you ready to run this program?")
    run_choice = input("Y - Yes, N - No: ")
    print()

    while run_choice == 'Y' or run_choice == 'y':
        input_char = (input("Enter a character: "))
        converted_char = ord(input_char)
        print("The ASCII code for {} is {}.".format(input_char,converted_char))
        print()

        input_num = get_number(LOWER, UPPER)

        if LOWER <= input_num <= UPPER:
            converted_num = chr(input_num)
            print("The character for {} is {}.".format(input_num,converted_num))
            print()

        print("Would you like to run this program again?")
        run_choice = input("Y - Yes, N - No: ")
        print()

    print('An ASCII Table has been provided below:')

    for i in range(33,128,1):
        char = chr(i)
        print('{:>3}  {}'.format(i,char))


    print()
    print("Goodbye.")


def get_number(lower, upper):
    valid_number = False
    while not valid_number:
        number = int(input("Enter a number ({}-{}): ".format(lower, upper)))
        #if lower < number < upper:
        if number > lower and number < upper:
            valid_number = True
        else:
            print("Please enter a valid number!")
            print("")
    return number

main()















