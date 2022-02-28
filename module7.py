# parent class for each entry
class FeedEntryClass:
    # initialize FeedEntryClass
    def __init__(self, name):
        # place class name parameter to a variable
        self.name = name
        # set path to the file
        self.path = 'feed/feed.txt'
        # get current date and time
        self.now = datetime.datetime.now()
        # place to datetime string variable current date and time in required format
        self.datetime_string = self.now.strftime("%Y/%m/%d %H:%M")
        # place to date string variable current date in required format
        self.date_string = self.now.strftime("%Y/%m/%d")
        # initialize class variables
        self.message = ''
        self.location = ''
        self.feed_file = ''

    # write initial message to the file method
    def initial_message(self):
        # catch FileNotFoundError exception
        try:
            # check if file is empty
            if os.path.getsize(self.path) == 0:
                # open file for write
                self.feed_file = open(f'{self.path}', 'w')
                # write initial text
                self.feed_file.write('Latest posts\n')
                # close file to see results immediately
                self.feed_file.close()
        # process FileNotFoundError exception
        except FileNotFoundError:
            # print error message
            print("Error: Can't open target file 'feed/feed.txt'")
            input("Press ENTER to quit")
            # stop the script
            quit()

    # static method decorator
    @staticmethod
    # output status method
    def status(entry_type):
        # print status message to console
        print(f"\nNew {entry_type} entry has been SUCCESSFULLY added!")
        input("Press any key to continue...")

    # static method decorator
    @staticmethod
    # clear screen static method
    def cls():
        # base on os type define clear screen command
        os.system('cls' if os.name == 'nt' else 'clear')


# NewsClass, child from FeedEntryClass
class NewsClass(FeedEntryClass):
    # initialize NewsClass
    def __init__(self, name):
        # initialize parent class
        FeedEntryClass.__init__(self, 'General Feed')
        # place class name parameter to a variable
        self.name = name

    # add news to the file method
    def output(self, message, location):
        # create method variables
        self.message = message
        self.location = location
        # open file for append
        self.feed_file = open(f'{self.path}', 'a')
        # write to the file
        self.feed_file.write(f'\n{self.name} -------------------------\n')
        self.feed_file.write(self.message + '\n')
        self.feed_file.write(f'{self.location}, {str(self.datetime_string)}\n')
        self.feed_file.write('------------------------------\n')
        # close file to see results immediately
        self.feed_file.close()
        if user_interface.top_menu_input == '1':
            # write to console status message
            self.status(self.name)
            # clear screen
            self.cls()


# AdvClass, child from FeedEntryClass
class AdvClass(FeedEntryClass):
    # initialize AdvClass
    def __init__(self, name):
        # initialize parent class
        FeedEntryClass.__init__(self, 'General Feed')
        # initialize class variable
        self.expiration_date = ''
        # place class name parameter to a variable
        self.name = name

    # static method decorator
    @staticmethod
    # calculate expiration days for the advertisement
    def expiration_days(self, expiration_date):
        # create method variables
        self.expiration_date = expiration_date
        # create a date object from the input parameter string
        self.expiration_date = datetime.datetime.strptime(self.expiration_date, "%Y/%m/%d")
        # return number of days between expiration date and current date
        return abs((self.expiration_date - self.now).days)

    # add advertising to the file method
    def output(self, message, expiration_date):
        self.expiration_date = expiration_date
        # open file for append
        self.feed_file = open(f'{self.path}', 'a')
        # write to the file
        self.feed_file.write(f'\n{self.name} -------------------\n')
        self.feed_file.write(message + '\n')
        self.feed_file.write(f'Actual until: {self.expiration_date}, '
                             f'{str(self.expiration_days(self, self.expiration_date))} '
                             f'days left')
        self.feed_file.write('\n------------------------------\n')
        # close file to see results immediately
        self.feed_file.close()
        # if manual input
        if user_interface.top_menu_input == '1':
            # write to console status message
            self.status(self.name)
            # clear screen
            self.cls()


# WeatherForecastClass, child from FeedEntryClass
class WeatherForecastClass(FeedEntryClass):
    # initialize AdvClass
    def __init__(self, name):
        # initialize parent class
        FeedEntryClass.__init__(self, 'General Feed')
        # place class name parameter to a variable
        self.name = name
        # variable to store degree sign
        self.degree_sign = u"\N{DEGREE SIGN}"
        # variable with next day date
        self.next_day = self.now + datetime.timedelta(days=1)
        # initialize class variable
        self.temperature = ''

    # add weather forecast for tomorrow to the file method
    def output(self, location, summary, temperature):
        # create method variables
        self.message = summary
        self.location = location
        self.temperature = temperature
        # open file for append
        self.feed_file = open(f'{self.path}', 'a')
        # write to the file
        self.feed_file.write(f'\n{self.name} -------------\n')
        self.feed_file.write(f'Forecast date: {self.next_day.strftime("%Y/%m/%d")}\n')
        self.feed_file.write(f'Location: {self.location}\n')
        self.feed_file.write(f'Summary: {self.message}\n')
        self.feed_file.write(f'Forecast temperature: {self.temperature}{self.degree_sign}C')
        self.feed_file.write('\n------------------------------\n')
        # close file to see results immediately
        self.feed_file.close()
        if user_interface.top_menu_input == '1':
            # write to console status message
            self.status(self.name)
            # clear screen
            self.cls()


# VerificationClass, child from FeedEntryClass
class VerificationClass(FeedEntryClass):
    # initialize VerificationClass
    def __init__(self):
        # initialize parent class
        FeedEntryClass.__init__(self, 'General Feed')
        # initialize class variables
        self.correct_format_date = ''
        self.temperature_to_check = ''
        self.date_to_check = ''
        self.string_to_check = ''
        # pattern for temperature range or a single temperature value
        self.ends_with_number_pattern = re.compile(r'^[\\+\-\s\d]*\d+$')

    # verify temperature method
    def verify_temperature(self, temperature_to_check):
        self.temperature_to_check = temperature_to_check
        # if temperature string contains allowed symbols and ends with a number
        if self.ends_with_number_pattern.search(self.temperature_to_check):
            return True
        else:
            return False

    # verify date method
    def verify_date(self, date_to_check):
        self.date_to_check = date_to_check
        # catch ValueError exception
        try:
            # create a date object from the input parameter string
            self.correct_format_date = datetime.datetime.strptime(self.date_to_check, '%Y/%m/%d')
            # check if current date is earlier then expiration date
            if self.date_to_check < self.date_string:
                # print error message
                print("Error: You have entered date in the past")
                return False
            # if date corresponds all requirements
            else:
                return True
        # process ValueError exception
        except ValueError:
            return False

    # verify empty input method
    def verify_empty_input(self, string_to_check):
        self.string_to_check = string_to_check
        # check string length
        if len(self.string_to_check) > 0:
            return True
        else:
            return False


# Batch load class
class BatchLoadClass:
    # Initialize BatchLoadClass
    def __init__(self, path):
        self.path = path
        self.batch_file = ''
        self.file_text = ''
        self.parse_lines = ''
        self.parse_line = ''
        self.invalid_record = 0
        self.records_number = 0
        self.file_dir = ''
        self.invalid_file = ''
        self.par2 = ''
        self.par3 = ''
        self.par4 = ''

    # set default path to a batch file
    def get_path(self):
        if self.path == '':
            self.path = 'feed/batch.txt'

    # verify file location
    def open_dir(self):
        # catch FileNotFoundError exception
        try:
            # check if file is empty
            if os.path.getsize(self.path) == 0:
                print('empty file')
            else:
                # open file for write
                self.batch_file = open(f'{self.path}', 'r')
                self.file_text = self.batch_file.read()
                # close file to see results immediately
                self.batch_file.close()
        # process FileNotFoundError exception
        except FileNotFoundError:
            # print error message
            print(f"Error: Can't open target file {self.path}")
            input("Press ENTER to quit")
            # stop the script
            quit()
        return self.file_text

    # batch file parser
    def batch_parser(self, batch_file):
        # batch file pointer
        self.batch_file = batch_file
        # divide into lines
        self.parse_lines = self.batch_file.split('\n')
        # define directory
        self.file_dir = os.path.dirname(f'{self.path}')
        # iterate through records
        for i in self.parse_lines:
            # split record into fields
            self.parse_line = i.split('\t|\t')
            # look for beginning of weather forecast record
            if re.search('^Weather forecast$', self.parse_line[0]):
                # create WeatherForecastClass class object
                wfc = WeatherForecastClass('Weather forecast')
                try:
                    # call wfc.output method
                    wfc.output(self.parse_line[1], self.parse_line[2], self.parse_line[3])
                    self.records_number += 1
                except IndexError:
                    print('Error: Incorrect record format in a batch file')
                    self.invalid_record += 1
                    # write to invalid file
                    self.invalid_file = open(f'{self.file_dir}/invalid_records.txt', 'a')
                    self.invalid_file.write(f'{feed.datetime_string}\t{self.parse_line}\n')
                    self.invalid_file.close()
            elif re.search('^Private Ad$', self.parse_line[0]):
                # create AdvClass class object
                adv = AdvClass('Private Ad')
                try:
                    # capitalize function
                    self.par2 = module4.capitalize_sentences(self.parse_line[1])
                    # verify date
                    vrf = VerificationClass()
                    if not vrf.verify_date(self.parse_line[2]):
                        # write to invalid file
                        self.invalid_file = open(f'{self.file_dir}/invalid_records.txt', 'a')
                        self.invalid_file.write(f'{feed.datetime_string}\t{self.parse_line}\n')
                        self.invalid_file.close()
                        self.invalid_record += 1
                    else:
                        # set parameter valus
                        self.par3 = self.parse_line[2]
                        # call adv.output method
                        adv.output(self.par2, self.par3)
                        self.records_number += 1
                except IndexError:
                    print('Error: Incorrect record format in a batch file')
                    # write to invalid file
                    self.invalid_file = open(f'{self.file_dir}/invalid_records.txt', 'a')
                    self.invalid_file.write(f'{feed.datetime_string}\t{self.parse_line}\n')
                    self.invalid_file.close()
                    self.invalid_record += 1
            elif re.search('^News$', self.parse_line[0]):
                # create NewsClass class object
                nws = NewsClass('News')
                try:
                    # capitalize function
                    self.par2 = module4.capitalize_sentences(self.parse_line[1])
                    self.par3 = self.parse_line[2]
                    # call news.output method
                    nws.output(self.par2, self.par3)
                    self.records_number += 1
                except IndexError:
                    print('Error: Incorrect record format in a batch file')
                    self.invalid_record += 1
                    # write to invalid file
                    self.invalid_file = open(f'{self.file_dir}/invalid_records.txt', 'a')
                    self.invalid_file.write(f'{feed.datetime_string}\t{self.parse_line}\n')
                    self.invalid_file.close()
            else:
                print('Error: Unexpected feed type')
                self.invalid_record += 1
                # write to invalid file
                self.invalid_file = open(f'{self.file_dir}/invalid_records.txt', 'a')
                self.invalid_file.write(f'{feed.datetime_string}\t{self.parse_line}\n')
                self.invalid_file.close()
        # if there were parsed records
        if self.records_number > 0:
            # letter & word counts
            csv_obj = CsvClass(self.path)
            csv_obj.csv_output_words(csv_obj.word_count())
            csv_obj.csv_output_letters(csv_obj.letter_count())
        # if each record was parsed without errors
        if self.invalid_record == 0:
            # remove batch file
            os.remove(self.path)
        print(f'{self.records_number} records have been processed successfully. '
              f'Number of invalid records: {self.invalid_record}')
        input('\nPress Enter to continue')
        # clear screen
        feed.cls()


# Class for csv processing
class CsvClass:
    def __init__(self, path):
        self.feed_path = path
        self.csv_path = os.path.dirname(f'{path}')
        self.csv_file_words = 'word_count.csv'
        self.csv_file_letters = 'letter_count.csv'
        self.count_words_list = []
        self.feed_text = ''
        self.words_list = []
        self.distinct_words_list = []
        self.output_words_list = []
        self.distinct_letters_list = []
        self.output_letters_list = []
        self.to_csv_list = []
        self.parts = ''
        self.csv_row = ''
        self.all_letter_counter = 0
        self.upper_letter_counter = 0
        self.percentage = 0
        self.headers = []
        self.letter_dict = {}

    # word count method
    def word_count(self):
        with open(f'{self.feed_path}', 'r') as feed_text:
            self.feed_text = feed_text.read()
            # divide into words
            self.words_list = re.split(r'\s|\n', self.feed_text)
            for word in self.words_list:
                # take only alpha-num values
                if word.isalnum():
                    # if it's the first time we meet the word
                    if self.distinct_words_list.count(word) == 0:
                        # append to the list with unique words
                        self.distinct_words_list.append(word)
                        # append to the output list
                        self.output_words_list.append(f'{word} {self.words_list.count(word)}')
            return self.output_words_list

    # letter count method
    def letter_count(self):
        with open(f'{self.feed_path}', 'r') as feed_text:
            self.feed_text = feed_text.read()
            # divide into words
            self.words_list = re.split(r'\s|\n', self.feed_text)
            for word in self.words_list:
                # take only alpha-num values
                if word.isalnum():
                    for letter in word:
                        # if it's the first time we meet the letter
                        if letter.isalpha() and self.distinct_letters_list.count(f'{letter.lower()}') == 0:
                            # append letter to the distinct letters list
                            self.distinct_letters_list.append(letter.lower())
                            # define output values
                            self.all_letter_counter = self.feed_text.lower().count(f'{letter.lower()}')
                            self.upper_letter_counter = self.feed_text.count(f'{letter.upper()}')
                            self.percentage = round(self.all_letter_counter / len(self.feed_text) * 100, 2)
                            self.letter_dict = {'letter': letter.lower(),
                                                'count_all': self.all_letter_counter,
                                                'count_uppercase': self.upper_letter_counter,
                                                'percentage': self.percentage}
                            # append dictionary to the list
                            self.output_letters_list.append(self.letter_dict)
            return self.output_letters_list

    # words csv
    def csv_output_words(self, output_list):
        self.to_csv_list = output_list
        with open(f'{self.csv_path}/{self.csv_file_words}', 'w', newline='') as csv_file:
            writer_csv = csv.writer(csv_file, delimiter='-')
            for word in self.to_csv_list:
                self.parts = word.split(' ')
                writer_csv.writerow(self.parts)

    # letters csv
    def csv_output_letters(self, output_list):
        self.to_csv_list = output_list
        with open(f'{self.csv_path}/{self.csv_file_letters}', 'w', newline='') as csv_file:
            self.headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer_csv = csv.DictWriter(csv_file, delimiter=',', quotechar="'", fieldnames=self.headers)
            writer_csv.writeheader()
            for rows in self.to_csv_list:
                writer_csv.writerow(rows)


# User Interface Class
class UIClass:
    # initialize UIClass
    def __init__(self):
        # initialize class variables
        self.top_menu_input = '-1'
        self.menu_input = '-1'
        self.news_text_input = ''
        self.news_location_input = ''
        self.adv_text_input = ''
        self.expiration_date_input = ''
        self.forecast_location_input = ''
        self.forecast_summary_input = ''
        self.forecast_temperature_input = ''
        self.path_input = ''
        self.batch_file_content = ''

    # select menu option method
    def select_option(self):
        while self.menu_input not in ('0', '1', '2'):
            # print menu
            print("-" * 20)
            print("Select input type:")
            print("-" * 20, "\n")
            print("Press '1' to input feed entry manually")
            print("Press '2' for batch load")
            print("Press '0' to quit")
            # wait for user input
            self.top_menu_input = input("\n> ")
            if self.top_menu_input == '1':
                # wait for correct input
                while self.menu_input not in ('0', '1', '2', '3'):
                    # print menu
                    print("-" * 20)
                    print("Select feed entry:")
                    print("-" * 20, "\n")
                    print("Press '1' to publish News")
                    print("Press '2' to publish Advertising")
                    print("Press '3' to publish Weather forecast")
                    print("Press '0' to quit")
                    # wait for user input
                    self.menu_input = input("\n> ")
                # create VerificationClass class object
                vrf = VerificationClass()
                # News dialog
                if self.menu_input == '1':
                    # check user input for non empty string
                    while not vrf.verify_empty_input(self.news_text_input):
                        self.news_text_input = input("\nInput news text here\n> ")
                    # check user input for non empty string
                    while not vrf.verify_empty_input(self.news_location_input):
                        self.news_location_input = input("Input location please\n> ")
                    # create NewsClass class object
                    nws = NewsClass('News')
                    # call news_input method
                    nws.output(self.news_text_input, self.news_location_input)
                    # reset variables
                    self.news_text_input = ''
                    self.news_location_input = ''
                # Advertisement dialog
                elif self.menu_input == '2':
                    # check user input for non empty string
                    while not vrf.verify_empty_input(self.adv_text_input):
                        self.adv_text_input = input("\nInput advertising text here\n> ")
                    # check date validity
                    while not vrf.verify_date(self.expiration_date_input):
                        self.expiration_date_input = input("Input valid expiration date in format YYYY/MM/DD\n> ")
                    # create AdvClass class object
                    adv = AdvClass('Private Ad')
                    # call adv_input method
                    adv.output(self.adv_text_input, self.expiration_date_input)
                    # reset variables
                    self.adv_text_input = ''
                    self.expiration_date_input = ''
                # Weather forecast dialog
                elif self.menu_input == '3':
                    # check user input for non empty string
                    while not vrf.verify_empty_input(self.forecast_location_input):
                        self.forecast_location_input = input("\nInput forecast location please\n> ")
                    # check user input for non empty string
                    while not vrf.verify_empty_input(self.forecast_summary_input):
                        self.forecast_summary_input = input("Input forecast summary\n> ")
                    # check user input for non empty string
                    while not vrf.verify_temperature(self.forecast_temperature_input):
                        self.forecast_temperature_input = input("Input forecast temperature range. "
                                                                "Numbers and '+', '-', ' ' signs are allowed "
                                                                "(e. g. -1 +3)\n>")
                    # create WeatherForecastClass class object
                    wfc = WeatherForecastClass('Weather forecast')
                    # call wf_input method
                    wfc.output(self.forecast_location_input,
                               self.forecast_summary_input, self.forecast_temperature_input)
                    # reset variables
                    self.forecast_location_input = ''
                    self.forecast_summary_input = ''
                    self.forecast_temperature_input = ''
                # Quit dialog
                elif self.menu_input == '0':
                    # stop the script
                    quit()
                # reset menu_input variable
                self.menu_input = '-1'
            elif self.top_menu_input == '2':
                self.path_input = input(f"\nInput path to a file or press enter for default path value {feed.path}\n> ")
                bth = BatchLoadClass(self.path_input)
                bth.get_path()
                self.batch_file_content = bth.open_dir()
                bth.batch_parser(self.batch_file_content)
            elif self.top_menu_input == '0':
                # stop the script
                quit()


# check if it's an entry point
if __name__ == '__main__':
    # import os library to be able to clear console output and work with files
    import os
    # import datetime library to be able to clear console output and work with files
    import datetime
    # import re library to work with regex
    import re
    # import case normalizer
    import module4
    #
    import csv
    # create Feed object
    feed = FeedEntryClass('General Feed')
    # write initial message to the file
    feed.initial_message()
    # create UI object
    user_interface = UIClass()
    # loop input process
    while True:
        # get user's choice of CMS input option
        user_interface.select_option()
