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
        # write to console status message
        self.status(entry_type=self.name)
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


# User Interface Class
class UIClass:
    # initialize UIClass
    def __init__(self):
        # initialize class variables
        self.menu_input = '-1'
        self.news_text_input = ''
        self.news_location_input = ''
        self.adv_text_input = ''
        self.expiration_date_input = ''
        self.forecast_location_input = ''
        self.forecast_summary_input = ''
        self.forecast_temperature_input = ''

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
                                                        "Numbers and '+', '-', ' ' signs are allowed (e. g. -1 +3)\n>")
            # create WeatherForecastClass class object
            wfc = WeatherForecastClass('Weather forecast')
            # call wf_input method
            wfc.output(self.forecast_location_input, self.forecast_summary_input, self.forecast_temperature_input)
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


# check if it's an entry point
if __name__ == '__main__':
    # import os library to be able to clear console output and work with files
    import os
    # import datetime library to be able to clear console output and work with files
    import datetime
    # import re library to work with regex
    import re
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
