import sys
import xerox

def main():
	try:
		plainText = ""
		if (len(sys.argv) == 1):
			plainText = raw_input('Enter text -:\n')
		else:
			plainText = sys.argv[2]
	
		cipherText = plainText.encode('rot13')
		print cipherText
	
		xerox.copy(cipherText)
		print 'Copied to clipboard!!'
	except Exception as exception:
		errorMessage = "Error : " + exception.message
		print errorMessage

if __name__ == '__main__':
	main()
