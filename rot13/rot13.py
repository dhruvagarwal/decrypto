import xerox
ans=raw_input('Enter text for rot13 - ').encode('rot13')
print ans
xerox.copy(ans)
print 'Copied to clipboard'
