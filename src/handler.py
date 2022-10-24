from .generator import Generator
from .input_handler import InputHandler
from .output_handler import OutputHandler


class Handler:
    data_type = {
        1: {"name": "Firstname", "file": False},
        2: {"name": "Lastname", "file": "lastname.txt"},
        3: {"name": "Email", "file": False},
        4: {"name": "City", "file": "geo_city.txt"},
        5: {"name": "Address", "file": False},
        6: {"name": "Title", "file": False},
        7: {"name": "Description", "file": False},
        8: {"name": "Datetime", "file": False},
    }

    def __init__(self):
        data_type = self.data_type
        self.generator = Generator(data_type)
        self.input_handler = InputHandler(data_type)
        self.output_handler = OutputHandler()

    def run(self):
        table_name = self.input_handler.get_table_name()

        # Handle user input
        data = self.input_handler.handle_input()

        # Generate Data
        results = self.generator.generate(data, 50)

        self.output_handler.print_output(table_name, results)
