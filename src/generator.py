import os
import random


class Generator:
    data_type = {}

    def __init__(self, data_type):
        self.data_type = data_type

    def generate(self, data, generation_amount=2):

        result = {}

        for i in data:
            item = data.get(i)
            col_name = item.get("name")
            data_object = self.data_type.get(item.get("type"))
            data_type = data_object.get("file")
            counter = 0
            values = []

            while counter < generation_amount:
                if data_type is False:
                    rand = self.handle_special_case(data_object.get("name").lower())
                    values.append(rand.replace("'", ""))
                else:
                    rand = self.get_random_pick_from_file("name_male.txt")
                    values.append(rand.replace("'", ""))
                counter += 1

            result[col_name] = values
        return result

    def handle_special_case(self, data_type):
        if data_type == 'firstname':
            return self.generate_firstname()
        if data_type == "email":
            return self.generate_email()
        if data_type == "address":
            return self.generate_address()
        if data_type == "title":
            return self.generate_random_words(7)
        if data_type == "description":
            return self.generate_random_words(150)
        if data_type == "datetime":
            return self.generate_datetime()

    def get_random_pick_from_file(self, file_name):
        base_path = os.path.abspath('.')
        return random.choice(list(open(base_path + '/data/' + file_name, encoding="utf8"))).strip()

    def generate_firstname(self):
        files = ["name_female.txt", "name_male.txt"]
        return self.get_random_pick_from_file(random.choice(files))

    def generate_email(self):
        files = ["name_female.txt", "name_male.txt"]
        firstname = self.get_random_pick_from_file(random.choice(files)).lower()
        lastname = self.get_random_pick_from_file('name_last.txt').lower()
        mail_domain = self.get_random_pick_from_file('mail_company.txt')
        mail_ext = self.get_random_pick_from_file('web_extensions.txt')
        mail = "{}.{}".format(mail_domain, mail_ext)
        randomizer = random.randint(0, 9)
        value = random.randint(1, 99)

        if randomizer == 0:
            return "{}{}@{}".format(firstname, lastname, mail)
        elif randomizer == 1:
            return "{}{}{}@{}".format(firstname, lastname, value, mail)
        elif randomizer == 2:
            return "{}.{}@{}".format(firstname, lastname, mail)
        elif randomizer == 3:
            return "{}.{}{}@{}".format(firstname, lastname, value, mail)
        elif randomizer == 4:
            return "{}_{}@{}".format(firstname, lastname, mail)
        elif randomizer == 5:
            return "{}_{}{}@{}".format(firstname, lastname, value, mail)
        elif randomizer == 6:
            return "{}{}@{}".format(firstname, lastname, mail)
        elif randomizer == 7:
            return "{}{}{}@{}".format(firstname, lastname, value, mail)
        elif randomizer == 8:
            return "{}{}@{}".format(lastname, value, mail)
        else:
            return "{}@{}".format(lastname, mail)

    def generate_address(self):
        city = self.get_random_pick_from_file('geo_city.txt')
        country = self.get_random_pick_from_file('geo_country.txt')
        road = self.get_random_pick_from_file('geo_street.txt')
        return "{} {}, {} {} {}".format(
            random.randint(1, 999),
            road,
            random.randint(1000, 99999),
            city,
            country,
        )

    def generate_random_words(self, max_words, min_words = 1):
        words = []
        for i in range(random.randint(min_words, max_words)):
            words.append(self.get_random_pick_from_file('random_words.txt'))
        return ' '.join(words)

    def generate_datetime(self):
        return "{}-{}-{} {}:{}:{}".format(
            random.randint(2000, 2024),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59),
        )

