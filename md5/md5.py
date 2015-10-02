import sys
import hashlib
import xerox

def main():
    try:
        text = ""
        if (len(sys.argv) == 1):
            text = raw_input('Enter text -:\n')
        else:
            text = sys.argv[1]
        	
        text_hash = hashlib.md5(text).hexdigest()
        print text_hash
        	
        xerox.copy(text_hash)
        print 'Copied to clipboard!!'
    except Exception as exception:
        print "Error : {exception}".format(exception=exception.message)

if __name__ == '__main__':
    main()
