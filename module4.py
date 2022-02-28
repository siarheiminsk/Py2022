# catch module import error
try:
    # import re module to use regexp
    import re
    # import sys module to be able to stop script execution
    import sys
    # import os module to be able to clear console output
    import os
    # import methods from colorama module to add some colours to output
    from colorama import init, Fore, Back, Style
# handle module import error
except ImportError as imp_err:
    # print error message
    print("Error: " + str(imp_err) + ". Please install all required modules: re, sys, os, colorama")
    # wait user's input
    input("")
    # stop the script
    sys.exit(1)

# initialise Colorama
init()

# set initial string
initial_string = r"""
homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# last words of every paragraph, which ends with a full stop function
def new_sentence_from_last_words(text):
    # set match counter
    match_count = 0
    # set list for last word of every paragraph
    paragraphs_last_word_list = []
    # pattern to search for a last word in a paragraph
    last_word_pattern = re.compile(r'(\w+)\.*\n')
    # find matches for last word in all paragraphs
    last_word_matches = re.findall(last_word_pattern, text)
    # iterate through matches
    while match_count < len(last_word_matches):
        # add matched word to a list
        paragraphs_last_word_list.append(str(last_word_matches[match_count]).lower())
        # increment match counter
        match_count = match_count + 1
    # add all last words divided by spaces to one string and capitalize the first letter
    paragraph_last_words_string = ' '.join(paragraphs_last_word_list).capitalize()
    # add initial space and terminating full stop
    new_sentence = f" {paragraph_last_words_string}."
    # return the result
    return new_sentence


# first letter of every paragraph and every sentence capitalized with saving paragraph indent function
def capitalize_sentences(text):
    # initiate list for all paragraphs
    paragraph_list = []
    # initiate string for all paragraphs
    paragraph_string = []
    # find all matches for a paragraph's indent and content
    all_matches = text.split('\n')
    # iterate through matches
    for paragraph_matches in all_matches:
        # split paragraph on sentences
        sentence_list = paragraph_matches.split('. ')
        for sentence in sentence_list:
            # add capitalized sentence to a sentence list
            paragraph_list.append(sentence.capitalize())
            x = re.search('[.!]$', sentence)
            # check for a full stop after a sentence
            if not x:
                # add a full stop
                paragraph_list.append('. ')
        # join paragraph's sentences to one string
        paragraph_string = ''.join(paragraph_list)
    return paragraph_string


# custom replacements function
def replacements(paragraph_string, substitutes):
    # iterate through defined replacements
    for replacement in substitutes:
        # replace grammar and punctuation mistakes
        paragraph_string = paragraph_string.replace(*replacement)
    return paragraph_string


# output results function
def output(header, param_string):
    # OUTPUT THE RESULT
    # count all whitespaces in the string
    whitespaces_count = str(len(re.findall(r'\s', param_string)))
    # set colours, print coloured section header and reset style
    print(f"\n{Back.GREEN}{Fore.BLACK}{header} string: {Style.RESET_ALL}\n")
    # print the string
    print(param_string + '\n')
    print("-" * 45)
    # print number of whitespaces for the string
    print(f"Whitespaces count for the {header} string: {whitespaces_count}\n\n\n")

# call function to make all sentences capitalized
cap_sentences = capitalize_sentences(initial_string)
