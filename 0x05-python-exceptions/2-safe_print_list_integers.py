#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_printed = 0
    for item in range(x):
            try:
                print("{:d}".format(item), end=' ')
                int_printed += 1
            except (ValueError, TypeError):
                pass
    print()
    return int_printed
