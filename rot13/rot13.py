import xerox
import string
rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
s=raw_input('Enter text for rot13 - ')
print string.translate(s, rot13)
xerox.copy(string.translate(s, rot13))
