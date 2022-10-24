class OutputHandler:

    def print_output(self, table_name, data):
        keys = list(data.keys())
        total_count = len(data.get(keys[0]))

        print("INSERT INTO `{}`".format(table_name))
        print("({})".format(', '.join(keys)))
        print("VALUES")

        for i in range(total_count):
            results = []
            for key in keys:
                results.append("'{}'".format(data.get(key)[i]))
            if i == total_count - 1:
                pass
                print("({})".format(', '.join(results)))
            else:
                pass
                print("({}),".format(', '.join(results)))

        print(";")
