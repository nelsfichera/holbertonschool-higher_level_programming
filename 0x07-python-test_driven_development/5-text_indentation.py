#!/usr/bin/python3
'''Manipulates text'''


def text_indentation(text):
    '''Prints text with indentation
    and removes extra spaces.Adds new lines
    after special characters. Takes
    one string argument, and raises
    an error when it is not a string.
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    character = 0
    text = text.strip(' ')

    while character < len(text):
        print(text[character], end='')

        if text[character] in (".", "?", ":"):
            if (character + 1) < len(text):
                while text[character + 1] == ' ':
                    character += 1
            print("\n")
        character += 1
