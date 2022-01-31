# catch module import error
try:
    # import sys module to be able to stop script execution
    import sys
    # import random module to generate random numbers
    import random
    # import string module to generate alphabet
    import string
    # import os module to be able to clear console output
    import os
    # import methods from colorama module to add some colours to output
    from colorama import init, Fore, Back, Style
# handle module import error
except ImportError as imp_err:
    # print error message
    print("Error: " + str(imp_err) + ". Please install all required modules: sys, random, string, os, colorama")
    # wait user's input
    input("")
    # stop the script
    sys.exit(1)

# initialise Colorama
init()


# clear screen function
def cls():
    # base on os type define clear screen command
    os.system('cls' if os.name == 'nt' else 'clear')


# make the script run as many times as user would like
while True:

    # ADD VARIABLES

    # dictionary for randomly generated items
    rand_dict = {}
    # list of all randomly generated dictionaries
    dict_list = []
    # aggregated dictionary
    agg_dict = {}
    # number of current dictionary
    dict_number = 0

    # generate random value from 2 to 10 for number of dictionaries
    dicts_number = random.randint(2, 10)
    # generate random value from 1 to total number of lowercase letters in english alphabet
    elements_number = random.randint(1, len(string.ascii_lowercase))

    # set colours, print coloured section header and reset style
    print("\n" + Back.GREEN, Fore.BLACK + "Settings: " + Style.RESET_ALL + '\n')
    # print number of dictionaries
    print('Number of dictionaries =', dicts_number)
    # print number of elements in each dictionary
    print('Number of elements =', elements_number)

    # GENERATE RANDOM DICTIONARIES

    # iterate as many times as many dictionaries we need
    for ii in range(dicts_number):
        # iterate as many times as many items in a dictionary we need
        while len(rand_dict) < elements_number:
            # generate dictionary item with randomly generated lowercase letter as a key
            rand_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        # add the dictionary copy to the list
        dict_list.append(rand_dict.copy())
        # clear the dictionary for future use
        rand_dict.clear()

    # set colours, print coloured section header and reset style
    print("\n" + Back.GREEN, Fore.BLACK + "Generated random dictionaries: " + Style.RESET_ALL + '\n')
    # print generated dictionaries
    for d in dict_list:
        print(d)

    # CREATE AN AGGREGATED DICTIONARY

    # iterate through the dictionaries list
    for d in dict_list:
        # iterate through same keys in all dictionaries
        for key_name in (list(d.keys())):
            # reset parameters
            # set maximal value for particular key
            max_value = 0
            # set current dictionary number
            dict_entry = 0
            # iterate through all dictionaries
            for i in range(len(dict_list)):
                # if the key exists in the dictionary
                if dict_list[i].get(key_name) is not None:
                    # compare current value with max_value
                    if dict_list[i].get(key_name) > max_value:
                        # set new max_value
                        max_value = dict_list[i].get(key_name)
                        # save current dictionary number
                        dict_entry = i
                        # increment to determine non unique keys
                        dict_number += 1
                    else:
                        # increment to determine non unique keys
                        dict_number += 1
            # if the key is unique
            if dict_number == 1:
                # write to aggregated dictionary key name without the dictionary number
                agg_dict[key_name] = max_value
            # if the key is non unique
            else:
                # write to aggregated dictionary key name with the dictionary number
                agg_dict[key_name + '_' + str(dict_entry+1)] = max_value
            # reset variable for future use
            dict_number = 0

    # set colours, print coloured section header and reset style
    print("\n" + Back.GREEN, Fore.BLACK + "Aggregated dictionary: " + Style.RESET_ALL + '\n')
    # print the aggregated dictionary
    print(agg_dict)

    # print menu message
    print("\n" * 3)
    print("-" * 52)
    print("-- Input " + Back.GREEN, Fore.BLACK + "Q " + Style.RESET_ALL + " to quit or press "
          + Back.GREEN, Fore.BLACK + "ENTER " + Style.RESET_ALL + " to continue --")
    print("-" * 52)
    # save user's choice
    menu = input("> ")
    # if user inputs q or Q
    if menu == 'Q' or menu == 'q':
        # end script
        quit()
    # clear console output
    cls()
