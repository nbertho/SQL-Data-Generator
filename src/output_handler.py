class OutputHandler:

    def print_output(self, table_name, data):
        keys = list(data.keys())

        print("INSERT INTO `{}`".format(table_name))
        print("({})".format(', '.join(keys)))
        print("VALUES")

        for i in range(len(keys)):
            results = []
            for key in keys:
                results.append("'{}'".format(data.get(key)[i]))
            print("({})".format(', '.join(results)))

        print(";")
