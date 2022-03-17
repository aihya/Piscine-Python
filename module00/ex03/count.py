import string

def text_analyzer(*args):
    """
This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.

If more than one argument was provided the function prints "ERROR".
If no argument was provided, it will prompt the user to enter some text.
"""
    if len(args) > 1:
        print("ERROR")
        return

    text = ""
    if len(args) == 0:
        print("What is the text to analyse?")
        text = input(">> ")
    else:
        text = args[0]

    lcases = 0
    ucases = 0
    puncts = 0
    spaces = 0
    count = 0

    for c in text:
        count += 1
        if c in string.ascii_lowercase:
            lcases += 1
        elif c in string.ascii_uppercase:
            ucases += 1
        elif c == ' ':
            spaces += 1
        elif c in string.punctuation:
            puncts += 1

    print("The text contains {} characters:".format(count))
    print("- {} upper letters".format(ucases))
    print("- {} lower letters".format(lcases))
    print("- {} punctuation marks".format(puncts))
    print("- {} spaces".format(spaces))