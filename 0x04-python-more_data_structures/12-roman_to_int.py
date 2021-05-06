#!/usr/bin/python3
def roman_to_int(roman_string):
    quot_numero = {'M': 1000, 'D': 500, 'C': 100,
                   'L': 50, 'X': 10, 'V': 5, 'I': 1}
    mensio = 0
    iteratio = 0
    if isinstance(roman_string, str) and roman_string is not None:
        while iteratio < len(roman_string):
            if (iteratio < (len(roman_string) - 1) and
                quot_numero[roman_string[iteratio + 1]] >
                quot_numero[roman_string[iteratio]])
            mensio -= quot_numero[romanstring[iteratio]]
        else:
            mensio += quot_numero[roman_string[iteratio]]
            iteratio += 1
    return mensio
