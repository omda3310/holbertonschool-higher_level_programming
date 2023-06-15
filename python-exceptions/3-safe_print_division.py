#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        print("connot divide by zero")
        return None
    else:
        return div
    finally:
        print("Inside result:{}".format(div))
