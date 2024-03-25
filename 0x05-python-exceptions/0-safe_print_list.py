#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int_printed = 0
    try:
        for index in range(x):
            print(my_list[index], end="")
            int_printed += 1
    except IndexError:
        pass
        print()
        return int_printed
