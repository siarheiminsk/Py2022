import glob


class TestProcessor:
    def __init__(self, config, connector, logger):
        self.config = config
        self.connector = connector
        self.logger = logger

    def process(self):
        test_data_files = self.check_data_folder()

        for f in test_data_files:
            self.do_testing(f)

    def check_data_folder(self):
        test_data_folder = self.config.get_test_data_folder()
        return[f for f in glob.glob(test_data_folder + '/*.json', recursive=True)]

    def do_testing(self, file_name):
        self.logger.start_test(file_name)

        with open(file_name) as f:
            test_data = eval(f.read())

        for test in test_data['tests']:
            self.logger.start_case(test['name'])

            query = test['query']
            expected_result = test['result']
            actual_result = self.connector.execute(query)

            if actual_result == expected_result:
                self.logger.add_pass(query, actual_result)

            else:
                self.logger.add_fail(query, actual_result, expected_result)

        for test in test_data['common_tests']:
            self.logger.start_case(test['name'])

            query = test['query']
            schema = test['schema']
            table = test['table']
            expected_result = test['result']

            self.scope = self.connector.execute_sql(schema, table)

            for t in self.scope:
                sub_query=''
                sub_query = query+t[0]+"."+t[1]
                actual_result = self.connector.execute(sub_query)

                if actual_result >= expected_result:
                    self.logger.add_pass_common(sub_query, actual_result)

                else:
                    self.logger.add_fail_common(sub_query, actual_result, expected_result)


            self.logger.finish_test(file_name)
