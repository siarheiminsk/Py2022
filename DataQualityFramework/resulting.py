

class Result:
    def __init__(self):
        self.result_file = open('result/result.log', 'w')

    def start_test(self, file_name):
        self.result_file.write('--------------------------------------------\n'
                               'Testing of {} was started'
                               '\n--------------------------------------------'.format(file_name))

    def start_case(self, test_name):
        self.result_file.write('\n\n\n----'
                               'Testing case: {}\n'.format(test_name))

    def add_pass(self, query, actual_result):
        self.result_file.write("\nPASS. Result is {0} as expected"
                               "\n\tQuery: {1}".format(actual_result, query))

    def add_fail(self, query, actual_result, expected_result):
        self.result_file.write("\nFAIL. Result is {1} but expected {2}"
                               "\n\tQuery: {0}".format(query, actual_result, expected_result))

    def add_pass_common(self, sub_query, actual_result):
        self.result_file.write("\nPASS. Result is {0} as expected"
                               "\n\tQuery: {1}".format(actual_result, sub_query))

    def add_fail_common(self, sub_query, actual_result, expected_result):
        self.result_file.write("\nFAIL. Result is {1} but expected >= {2}"
                               "\n\tQuery: {0}".format(sub_query, actual_result, expected_result))

    def finish_test(self, file_name):
        self.result_file.write('\n\n--------------------------------------------\n'
                               'Testing of {} was finished'
                               '\n--------------------------------------------'.format(file_name))

    def close_file(self):
        self.result_file.close()