# import os library to be able to clear console output and work with files
import os
# import datetime library to be able to clear console output and work with files
import datetime
# import re library to work with regex
import re


# parent class for each entry
class FeedEntryClass:
    # initialize FeedEntryClass
    def __init__(self):
        # set path to the file
        self.path = 'feed/feed.txt'
        # get current date and time
        self.now = datetime.datetime.now()
        # place to datetime_string variable current date and time in required format
        self.datetime_string = self.now.strftime("%Y/%m/%d %H:%M")
        # initialize variables for future use
        self.message = ''
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
    def __init__(self):
        # initialize parent class
        FeedEntryClass.__init__(self)
        # initialize variables for future use
        self.news_text = ''
        self.news_location = ''

    # add news to the file method
    def news_input(self, message, location):
        # open file for append
        self.feed_file = open(f'{self.path}', 'a')
        # write to the file
        self.feed_file.write('\nNews -------------------------\n')
        self.feed_file.write(message + '\n')
        self.feed_file.write(f'{location}, {str(self.datetime_string)}\n')
        self.feed_file.write('------------------------------\n')
        # close file to see results immediately
        self.feed_file.close()
        # write to console status message
        self.status(entry_type='News')
        # clear screen
        self.cls()


# AdvClass, child from FeedEntryClass
class AdvClass(FeedEntryClass):
    # initialize AdvClass
    def __init__(self):
        # initialize parent class
        FeedEntryClass.__init__(self)
        # initialize variables for future use
        self.expiration_date = ''
        self.adv_text = ''

    # static method decorator
    @staticmethod
    # calculate expiration days for the advertisement
    def expiration_days(date1, date2):
        # create a date object from the input parameter string
        date1 = datetime.datetime.strptime(date1, "%Y/%m/%d")
        # create a date object from the input parameter string
        date2 = datetime.datetime.strptime(date2, "%Y/%m/%d")
        # return number of days between expiration date and current date
        return abs((date2 - date1).days)

    # add advertising to the file method
    def adv_input(self, message, expiration_date):
        # open file for append
        self.feed_file = open(f'{self.path}', 'a')
        # write to the file
        self.feed_file.write('\nPrivate Ad -------------------\n')
        self.feed_file.write(message + '\n')
        self.feed_file.write(f'Actual until: {expiration_date}, '
                             f'{str(self.expiration_days(self.now.strftime("%Y/%m/%d"), expiration_date))} '
                             f'days left')
        self.feed_file.write('\n------------------------------\n')
        # close file to see results immediately
        self.feed_file.close()
        # write to console status message
        self.status(entry_type='Advertising')
        # clear screen
        self.cls()


# WeatherForecastClass, child from FeedEntryClass
class WeatherForecastClass(FeedEntryClass):
    # initialize AdvClass
    def __init__(self):
        # initialize parent class
        FeedEntryClass.__init__(self)
        # variable to store degree sign
        self.degree_sign = u"\N{DEGREE SIGN}"
        # variable with next day date
        self.next_day = self.now + datetime.timedelta(days=1)
        # initialize variables for future use
        self.forecast_location = ''
        self.forecast_summary = ''
        self.forecast_temperature = ''

    # add weather forecast for tomorrow to the file method
    def wf_input(self, location, summary, temperature):
        # open file for append
        self.feed_file = open(f'{self.path}', 'a')
        # write to the file
        self.feed_file.write('\nWeather forecast -------------\n')
        self.feed_file.write(f'Forecast date: {self.next_day.strftime("%Y/%m/%d")}\n')
        self.feed_file.write(f'Location: {location}\n')
        self.feed_file.write(f'Summary: {summary}\n')
        self.feed_file.write(f'Forecast temperature: {temperature}{self.degree_sign}C')
        self.feed_file.write('\n------------------------------\n')
        # close file to see results immediately
        self.feed_file.close()
        # write to console status message
        self.status(entry_type='Weather forecast')
        # clear screen
        self.cls()


# VerificationClass, child from FeedEntryClass
class VerificationClass(FeedEntryClass):
    # initialize VerificationClass
    def __init__(self):
        # initialize parent class
        FeedEntryClass.__init__(self)
        # initialize variables for future use
        self.correct_format_date = ''
        # pattern for temperature range or a single temperature value
        self.ends_with_number_pattern = re.compile(r'^[\\+\-\s\d]*\d+$')

    # verify temperature method
    def verify_temperature(self, temperature_to_check):
        # if temperature string contains allowed symbols and ends with a number
        if self.ends_with_number_pattern.search(temperature_to_check):
            return True
        else:
            return False

    # verify date method
    def verify_date(self, date_to_check):
        # catch ValueError exception
        try:
            # create a date object from the input parameter string
            self.correct_format_date = datetime.datetime.strptime(date_to_check, '%Y/%m/%d')
            # check if current date is earlier then expiration date
            if self.correct_format_date < self.now:
                # print error message
                print("Error: You have entered date in the past")
                return False
            # if date corresponds all requirements
            else:
                return True
        # process ValueError exception
        except ValueError:
            return False

    # static method
    @staticmethod
    # verify empty input method
    def verify_empty_input(string_to_check):
        # check string length
        if len(string_to_check) > 0:
            return True
        else:
            return False


# User Interface Class, child from NewsClass, AdvClass, WeatherForecastClass, VerificationClass
class UIClass(NewsClass, AdvClass, WeatherForecastClass, VerificationClass):
    # initialize UIClass
    def __init__(self):
        # initialize parent classes
        NewsClass.__init__(self)
        AdvClass.__init__(self)
        WeatherForecastClass.__init__(self)
        VerificationClass.__init__(self)
        # initialize variable for menu input
        self.menu_input = '-1'

    # select menu option method
    def select_option(self):
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
        # News dialog
        if self.menu_input == '1':
            # check user input for non empty string
            while not VerificationClass.verify_empty_input(self.news_text):
                self.news_text = input("\nInput news text here\n> ")
            # check user input for non empty string
            while not VerificationClass.verify_empty_input(self.news_location):
                self.news_location = input("Input location please\n> ")
            # call news_input method
            NewsClass.news_input(self, self.news_text, self.news_location)
            # reset variables
            self.news_text = ''
            self.news_location = ''
        # Advertisement dialog
        elif self.menu_input == '2':
            # check user input for non empty string
            while not VerificationClass.verify_empty_input(self.adv_text):
                self.adv_text = input("\nInput advertising text here\n> ")
            # check date validity
            while not VerificationClass.verify_date(self, self.expiration_date):
                self.expiration_date = input("Input valid expiration date in format YYYY/MM/DD\n> ")
            # call adv_input method
            AdvClass.adv_input(self, self.adv_text, self.expiration_date)
            # reset variables
            self.adv_text = ''
            self.expiration_date = ''
        # Weather forecast dialog
        elif self.menu_input == '3':
            # check user input for non empty string
            while not VerificationClass.verify_empty_input(self.forecast_location):
                self.forecast_location = input("\nInput forecast location please\n> ")
            # check user input for non empty string
            while not VerificationClass.verify_empty_input(self.forecast_summary):
                self.forecast_summary = input("Input forecast summary\n> ")
            # check user input for non empty string
            while not VerificationClass.verify_temperature(self, self.forecast_temperature):
                self.forecast_temperature = input("Input forecast temperature range. "
                                                  "Numbers and '+', '-', ' ' signs are allowed (e. g. -1 +3)\n>")
            # call wf_input method
            WeatherForecastClass.wf_input(self, self.forecast_location,
                                          self.forecast_summary, self.forecast_temperature)
            # reset variables
            self.forecast_location = ''
            self.forecast_summary = ''
            self.forecast_temperature = ''
        # Quit dialog
        elif self.menu_input == '0':
            # stop the script
            quit()
        # reset menu_input variable
        self.menu_input = '-1'


# check if it's an entry point
if __name__ == '__main__':
    # create Feed object
    feed = FeedEntryClass()
    # write initial message to the file
    feed.initial_message()
    # create UI object
    user_interface = UIClass()
    # loop input process
    while True:
        # get user's choice of CMS input option
        user_interface.select_option()
