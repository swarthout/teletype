"""
TELE-TYPE

This is a program that encodes telephone word codes. It inputs a string of text and outputs an encrypted list of numbers. Each word is separated by a 0.
For example, if you input "I love computer programming", it will output 405683026678837077647266464.

BETA VERSION
Created by: Scott "Beamer" Swarthout
Notable Associates: Sophia "Cupcake" Farquhar
"""


def encode():
    text = input("Enter text to be encoded: ")
    text = text.lower()
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.replace("'","")
    def find_number(a):
        from string import ascii_lowercase
        keydict = {}
        for i in range(len(ascii_lowercase)):
            keydict[ascii_lowercase[i]] = ((i +(3-(i%3)))/3)+1
        keydict[" "] = 0
        keydict["s"] = 7
        keydict["v"] = 8
        keydict["y"] = 9
        keydict["z"] = 9
        message = []
        for i in a:
                message.append(int(keydict[i]))
        return ("".join(map(str, message)))
    print(find_number(text))
    encode()

encode()

