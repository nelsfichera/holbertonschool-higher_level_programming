#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = [0] * list_length
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except IndexError:
            result = 0
            print("out of range")
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        finally:
            result_list[x] = result
    return result_list
