#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    new_list = []
    while index < list_length:
        try:
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
            index += 1

    return new_list
