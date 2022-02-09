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


# output function
def output_f(header, param):
    # set colours, print coloured section header and reset style
    print(f"\n\n{Back.GREEN}{Fore.BLACK} {header} {Style.RESET_ALL}\n")
    print(param)


# generate random dictionaries function
def random_dictionaries(d_number, e_number):
    # dictionary for randomly generated items
    rand_dict = {}
    # list of all randomly generated dictionaries
    dict_list = []
    # iterate as many times as many dictionaries we need
    for ii in range(d_number):
        # iterate as many times as many items in a dictionary we need
        while len(rand_dict) < e_number:
            # generate dictionary item with randomly generated lowercase letter as a key
            rand_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        # add the dictionary copy to the list
        dict_list.append(rand_dict.copy())
        # clear the dictionary for future use
        rand_dict.clear()
    return dict_list


# create an aggregated dictionary function
def aggregated_dictionaries(d_list):
    # number of current dictionary
    dict_number = 0
    # aggregated dictionary
    agg_dict = {}
    # iterate through the dictionaries list
    for d in d_list:
        # iterate through same keys in all dictionaries
        for key_name in (list(d.keys())):
            # reset parameters
            # set maximal value for particular key
            max_value = 0
            # set current dictionary number
            dict_entry = 0
            # iterate through all dictionaries
            for i in range(len(d_list)):
                # if the key exists in the dictionary
                if d_list[i].get(key_name) is not None:
                    # compare current value with max_value
                    if d_list[i].get(key_name) > max_value:
                        # set new max_value
                        max_value = d_list[i].get(key_name)
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
    return agg_dict


# menu function
def menu():
    # print menu message
    print("\n" * 3)
    print("-" * 52)
    print(f"-- Input {Back.GREEN}{Fore.BLACK} Q {Style.RESET_ALL} to quit or press "
          f"{Back.GREEN}{Fore.BLACK} ENTER {Style.RESET_ALL} to continue --")
    print("-" * 52)
    # save user's choice
    user_input = input("> ")
    # if user inputs q or Q
    if user_input == 'Q' or user_input == 'q':
        # end script
        quit()
    # clear console output
    cls()


# make the script run as many times as user would like
while True:
    # generate random value from 2 to 10 for number of dictionaries
    dicts_number = random.randint(2, 10)
    # generate random value from 1 to total number of lowercase letters in english alphabet
    elements_number = random.randint(1, len(string.ascii_lowercase))
    # output generated parameters
    output_f(header='Settings: ', param=f'Number of dictionaries = {dicts_number}\n'
                                        f'Number of elements = {elements_number}')
    # generate list with defined number of dictionaries and elements
    random_dict_list = random_dictionaries(dicts_number, elements_number)
    # output generated dictionaries
    output_f(header='Generated random dictionaries: ', param=random_dict_list)
    # get aggregated dictionary
    aggregated_dictionary = aggregated_dictionaries(random_dict_list)
    # output aggregated dictionaries
    output_f(header='Aggregated dictionary: ', param=aggregated_dictionary)
    # print user's menu
    menu()
