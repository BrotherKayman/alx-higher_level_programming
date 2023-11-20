#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_printed = 0
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(item), end=' ')
                int_printed += 1
            except (ValueError, TypeError):
                pass
        print()
    except TypeError:
        return int_printed
    