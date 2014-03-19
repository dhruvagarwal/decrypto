import mechanize
from BeautifulSoup import BeautifulSoup
import xerox
d={'e':'encrypt','d':'decrypt'}
br=mechanize.Browser()
br.set_handle_robots(False)
ch=raw_input('Encrypt/Decrypt (e/d)? ')
ch=ch.lower()

br.open('http://www.md5online.org/md5-'+d[ch]+'.html')
br.select_form(nr=0)
br.form['md5']=raw_input('Enter text to '+d[ch]+' - ')
response=br.submit()
html=BeautifulSoup(''.join(response.read().split('\n')))

if ch=='d':
	l=html.find('span',style="color:limegreen").b.string
	print "Decrypted String is "+l
	xerox.copy(l)
	print 'Copied to ClipBoard!'
elif ch=='e':
	l=html.find('span',id="loading").b.string
	print "Encrypted String is "+l
	xerox.copy(l)
	print 'Copied to ClipBoard!'
else:
	print 'Error processing request'

