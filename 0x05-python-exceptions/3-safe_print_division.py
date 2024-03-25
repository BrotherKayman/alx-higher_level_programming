#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("{}".format(ans))
        return ans
