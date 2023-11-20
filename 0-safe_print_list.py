afe_print_list(my_list=[], x=0):
        int_printed = 0
            try:
                        for index in range(x):
                                        print("{}".format(my_list[index]), end="")
                                                    int_printed += 1
                                                        except IndexError:
                                                                    pass
                                                                    print('\n')
                                                                        return int_printed

