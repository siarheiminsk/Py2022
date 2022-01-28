# import random library to be able to generate random numbers
import random
# import os library to be able to clear console output
import os
# import methods from colorama library to add some colours to output
from colorama import init, Fore, Back, Style
# initialise Colorama
init()


# clear screen function
def cls():
    # base on os type define clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')


# make the script run as many times as user would like
while True:

    # ADD VARIABLES

    # list to store generated random numbers
    lst = []
    # int to store sum of even elements
    even_sum = 0
    # int to store number of even elements
    even_number = 0
    # int to store sum of odd elements
    odd_sum = 0
    # int to store number of odd elements
    odd_number = 0

    # default values
    # number of elements in a list
    lst_size = 100
    # minimum value in a range of random numbers
    min_value = 0
    # maximum value in a range of random numbers
    max_value = 1000

    # USER MENU TO SET CONFIGURATION PARAMETERS

    # initial value that doesn't match any menu option
    menu = -1
    # set colours, print coloured section header and reset style
    print("\n" + Back.GREEN, Fore.BLACK + "Please make your choice: " + Style.RESET_ALL + '\n')
    # wait for valid option
    while menu not in ('0', '1', '2'):
        # user chooses desired scenario
        menu = input(
            # multiline string
            """Press 1 to set custom configuration parameters 
Press 2 to use default values
Press 0 to quit
> """)
    # code for custom configuration option
    if int(menu) == 1:

        # set number of elements in a list
        # add try section to process user input
        try:
            # user inputs number of elements in a list
            lst_size = int(input("\nPlease enter number of elements in a list\n> "))
        # process incorrect input
        except ValueError as ve:
            # print error message
            print(Back.RED, Fore.LIGHTWHITE_EX + "Error: " + str(ve) + Style.RESET_ALL)
            # print default value notification
            print(Back.GREEN, Fore.LIGHTWHITE_EX + "We'll substitute it with the default value \'100\'"
                  + Style.RESET_ALL)
            # set default value
            lst_size = 100

        # minimum generated value
        # add try section to process user input
        try:
            # user inputs minimum generated value
            min_value = int(input("Please enter minimum generated value\n> "))
        # process incorrect input
        except ValueError as ve:
            # print error message
            print(Back.RED, Fore.LIGHTWHITE_EX + "Error: " + str(ve) + Style.RESET_ALL)
            # print default value notification
            print(Back.GREEN, Fore.LIGHTWHITE_EX + "We'll substitute it with the default value \'0\'"
                  + Style.RESET_ALL)
            # set default value
            min_value = 0

        # maximum generated value
        # add try section to process user input
        try:
            # user inputs minimum generated value
            max_value = int(input("Please enter maximum generated value\n> "))
        # process incorrect input
        except ValueError as ve:
            # print error message
            print(Back.RED, Fore.LIGHTWHITE_EX + "Error: " + str(ve) + Style.RESET_ALL)
            # print default value notification
            print(Back.GREEN, Fore.LIGHTWHITE_EX + "We'll substitute it with the default value \'1000\'"
                  + Style.RESET_ALL)
            # set default value
            max_value = 1000

    # code for custom configuration option
    elif int(menu) == 2:
        # no code here, default values have already been set above
        pass
    # code for quit option
    else:
        # stop the script
        quit()

    # GENERATE LIST WITH RANDOM NUMBERS

    # iterate number of times equal to number of list elements
    for i in range(lst_size):
        # check for greater number to make randint() work correctly
        if min_value <= max_value:
            # add random number from 0 to 1000 to list
            lst.append(random.randint(min_value, max_value))
        # second scenario to make randint() work correctly
        else:
            # add random number from 0 to 1000 to list
            lst.append(random.randint(max_value, min_value))

    # set colours, print coloured section header and reset style
    print("\n" + Back.GREEN, Fore.BLACK + "Generated list: " + Style.RESET_ALL + '\n')
    # print unsorted list
    print(str(lst) + '\n')

    # SORT POPULATED LIST

    # add try section to catch exceptions
    try:
        # iterate number of times equal to number of list elements
        for i2 in range(lst_size):
            # process all elements from the last to the first
            for i in range(lst_size - 1, 0, -1):
                # check if element exists and whether it should be processed
                if lst[i - 1] > lst[i]:
                    # swap elements: move greater one to the right
                    lst[i], lst[i - 1] = lst[i - 1], lst[i]
    # handle IndexError exception and place exception name to variable
    except IndexError as ie:
        # print custom error coloured red
        print(Back.RED, Fore.LIGHTWHITE_EX + "Error: " + str(ie) + Style.RESET_ALL)

    # set colours, print coloured section header and reset style
    print(Back.GREEN, Fore.BLACK + "Sorted list: " + Style.RESET_ALL + '\n')
    # print sorted list
    print(str(lst) + '\n')

    # CALCULATE AVERAGES

    # iterate through the list
    for i in lst:
        # check if the current element is an even number
        if i % 2 == 0:
            # increase total sum of even elements
            even_sum = even_sum + i
            # increase number of even elements
            even_number = even_number + 1
        # otherwise it's an odd element
        else:
            # increase total sum of odd elements
            odd_sum = odd_sum + i
            # increase number of odd elements
            odd_number = odd_number + 1

    # set colours, print coloured section header and reset style
    print(Back.GREEN, Fore.BLACK + "Averages: " + Style.RESET_ALL + '\n')

    # add try section to catch exceptions
    try:
        # check if there were any even numbers
        if even_number != 0:
            # print number of even elements and average for all even elements
            print("Average for", Fore.RED + str(even_number) + Style.RESET_ALL,
                  "even numbers is", Fore.RED + str(round(even_sum/even_number, 2)) + Style.RESET_ALL)
        # if there were no even numbers
        else:
            # print message
            print(Fore.RED + "There were no even numbers" + Style.RESET_ALL)

        # check if there were any odd numbers
        if odd_number:
            # print number of odd elements and average for all odd elements
            print("Average for", Fore.RED + str(odd_number) + Style.RESET_ALL,
                  "odd numbers is", Fore.RED + str(round(odd_sum/odd_number, 2)) + Style.RESET_ALL)
        # if there were no odd numbers
        else:
            # print message
            print(Fore.RED + "There were no odd numbers" + Style.RESET_ALL)

    # handle ZeroDivisionError exception and place exception name to variable
    except ZeroDivisionError as zde:
        # print custom error coloured red
        print(Back.RED, Fore.LIGHTWHITE_EX + "Error: " + str(zde) + Style.RESET_ALL)

    # wait for input to continue
    input("\nPress any key to continue")
    # clear console output
    cls()
