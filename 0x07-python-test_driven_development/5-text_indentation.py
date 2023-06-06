#!/usr/bin/python3

""" Module to print a text with 2 new lines after some special characters """


def text_indentation(text):
    """ Function to print 2 new lines after the characters '.', '?' and ':'

    Args:
        text: The text that we are to look from and print the new lines

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text = text.strip()
    """ To removee the trailing and leading whitespace in the printed lines """

    for character in text:
        """ Loop through the characters of the tect """

        print(character, end='')
        """ Print each character in the text """

        if character in['.', '?', ':']:
            """ To see if the character is among the special characters """

            print('\n\n', end='')
            """ If it is, print 2 new lines """

    print()
    """ Print a new line at the end """
