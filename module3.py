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

# ADD VARIABLES
# set initial string
initial_string = r"""
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# list of all paragraphs in initial string
paragraphs_list = []
# pattern to search for paragraph's indent
leading_spaces_pattern = re.compile(r'^(\s*)(.+)')
# pattern to search for a full stop in a paragraph
full_stop_spaces_pattern = re.compile(r'(\w+)\.\s*$')
# list with last words of each paragraph
paragraph_last_words_list = []
# string with last words of each paragraph
paragraph_last_words_string = ''
# final list with text transformations
final_list = []

# catch module import error
try:
    # INITIAL STRING PROCESSING
    # split initial string into paragraphs
    paragraphs = initial_string.split('\n')
    # iterate through all paragraphs
    for paragraph in paragraphs:
        # find all matches in a paragraph for leading_spaces_pattern
        all_matches = re.findall(leading_spaces_pattern, paragraph)
        # iterate through matches in a paragraph list
        for paragraph_matches in all_matches:
            # iterate through strings in matches in a paragraph list
            for part_match in paragraph_matches:
                # check if it's a paragraph with a sentence(-s)
                if part_match.endswith('.'):
                    # split paragraph on sentences
                    sentence_list = part_match.split('. ')
                    # iterate through every sentence
                    for sentence in sentence_list:
                        # add capitalized sentence to a sentence list
                        paragraphs_list.append(sentence.capitalize())
                        # check for a full stop after a sentence
                        if not sentence.endswith('.'):
                            # add a full stop
                            paragraphs_list.append('. ')
                # if it's a paragraph without sentences
                else:
                    # add capitalized sentence to a sentence list
                    paragraphs_list.append(part_match.capitalize())
            # join paragraph's sentences to one string
            paragraph_string = ''.join(paragraphs_list)
            # check for a paragraph to insert new sentence
            if re.search("add it to the end of this paragraph", paragraph_string) is not None:
                # add a paragraph string with a placeholder mark to a final list
                final_list.append(paragraph_string + ' <placeholder>.')
            # if there's no need to insert new sentence to this paragraph
            else:
                # add a paragraph string to a final list
                final_list.append(paragraph_string)
            # clear paragraph list
            paragraphs_list.clear()
        # find matches for last word in a paragraph
        last_word_matches = re.findall(full_stop_spaces_pattern, paragraph)
        # if there are any matches
        if last_word_matches:
            # add matched word to a list
            paragraph_last_words_list.append(str(last_word_matches[0]).lower())
        # add all last words to one string
        paragraph_last_words_string = ' '.join(paragraph_last_words_list).capitalize()
    # add new sentence to defined place
    final_string = ('\n\n'.join(final_list).replace('<placeholder>', paragraph_last_words_string))
    # set rules to replace grammar and punctuation mistakes
    for replacement in ((' iz', ' is'), ('x“iz', 'x “iz'), ('tex.', 'text.'), ('these text', 'this text')):
        # replace grammar and punctuation mistakes
        final_string = final_string.replace(*replacement)
except Exception as e:
    # print error message
    print("Unexpected error: ", str(e))

# count all whitespaces in the initial string
whitespaces_count_initial = str(len(re.findall(r'\s', initial_string)))
# count all whitespaces in the final string
whitespaces_count_final = str(len(re.findall(r'\s', final_string)))

# OUTPUT THE RESULT
# set colours, print coloured section header and reset style
print("\n" + Back.GREEN, Fore.BLACK + "Initial string: " + Style.RESET_ALL + "\n")
# print the initial string
print(initial_string+'\n')
print("-" * 45)
# print number of whitespaces for the initial string
print(f"Whitespaces count for the initial string: {whitespaces_count_initial}\n\n\n")
# set colours, print coloured section header and reset style
print("\n" + Back.GREEN, Fore.BLACK + "Final string: " + Style.RESET_ALL + "\n\n")
# print the final string
print(final_string+'\n')
print("-" * 45)
# print number of whitespaces for the final string
print(f"Whitespaces count for the final string: {whitespaces_count_final}\n\n\n\n")

# wait for user's input to finish the script
input("<< Press any key to finish >>")
