import sys

import xerox


def main():
    try:
        plaintext = ""
        if len(sys.argv) == 1:
            plaintext = raw_input('Enter text -:\n')
        else:
            plaintext = sys.argv[1]

        ciphertext = plaintext.encode('rot13')
        print ciphertext

        xerox.copy(ciphertext)
        print 'Copied to clipboard!!'
    except Exception as exception:
        print "Error : {exception}".format(exception=exception.message)

if __name__ == '__main__':
    main()
