import os


class InputHandler:
    phrases = {
        "COL_NAME_SELECT": "Select the name of the first column you want to generate\n\n",
        "COL_TYPE_SELECT": "Select the type of Data you want to generate (only numbers)",
        "COL_SAVE_ERROR": "!!! This column wont be saved, please try again\n\n",
        "ERR_INVALID_INT": "You must enter a valid number",
        "ERR_INVALID_TYPE_NMBR": "The number you typed was not in the list",
        "USER_VALIDATION": "Do you confirm? (Y/N)",
        "INVALID_CONFIRM_OPTION": "Please only enter one of the following character: y-n",
        "TABLE_NAME": "Please enter the name of your table"
    }

    data_type = {}

    generator_data = {}

    def __init__(self, data_type):
        self.data_type = data_type

    def handle_input(self):

        self.get_user_data()

        if self.confirm():
            return self.generator_data
        else:
            self.data_type = {}
            self.handle_input()

    def cls(self):
        """ Clear console """
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_col_name(self):
        """ Get col name or return False to continue """
        data_name = input(self.phrases.get("COL_NAME_SELECT"))

        if data_name == '':
            return None

        return data_name

    def get_data_type(self):
        """ Get data type """
        print(self.phrases.get('COL_TYPE_SELECT'))
        for key, item in self.data_type.items():
            print("    {} => {}".format(key, item.get("name")))

        data_type_nmbr = int(input())
        if data_type_nmbr not in self.data_type:
            raise ValueError(self.phrases.get("ERR_INVALID_TYPE_NMBR"))

        return data_type_nmbr

    def print_resume(self):
        for itemNumber in self.generator_data:
            data = self.generator_data.get(itemNumber)
            name = data.get("name")
            type = self.data_type.get(data.get("type")).get("name")
            print("Col {} : {} => {}".format(itemNumber, name, type))

    def confirm(self):
        true_options = ["y", "Y", "o", "O"]
        false_options = ["n", "N"]
        while True:
            print(self.phrases.get('USER_VALIDATION'))
            input_val = str(input())
            if input_val in true_options:
                return True
            elif input_val in false_options:
                return False
            else:
                print(self.phrases.get("INVALID_CONFIRM_OPTION"))

    def get_user_data(self):
        max_generation = 50
        counter = 0
        error_message = ""

        while True and counter <= max_generation:

            try:
                self.cls()
                if error_message != '':
                    print(error_message)
                    print(self.phrases.get("COL_SAVE_ERROR"))
                    error_message = ''

                data_name = self.get_col_name()
                if data_name is None:
                    break

                # Get the type of data
                data_type_nmbr = self.get_data_type()

                self.generator_data[str(counter)] = {
                    "name": data_name,
                    "type": data_type_nmbr
                }

                counter += 1

            except ValueError as err:
                error_message = err

        self.print_resume()

    def get_table_name(self):
        while True:
            print(self.phrases.get("TABLE_NAME"))
            table_name = str(input())
            if table_name != '':
                return table_name.strip()
