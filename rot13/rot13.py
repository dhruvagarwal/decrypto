import sys
import xerox

def main():
    try:
        plainText = ""
        if (len(sys.argv) == 1):
            plainText = raw_input('Enter text -:\n')
        else:
            plainText = sys.argv[1]
        	
        cipherText = plainText.encode('rot13')
        print cipherText
        	
        xerox.copy(cipherText)
        print 'Copied to clipboard!!'
    except Exception as exception:
        print "Error : {exception}".format(exception=exception.message)

if __name__ == '__main__':
    main()
