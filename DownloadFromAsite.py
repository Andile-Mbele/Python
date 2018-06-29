import urllib, sys

f = urllib.urlsopen("https://www.java2s.com")
while 1:
	buf  = f.read(2048)
	if not len(buf):
		break
	sys.stdout.write(buf)	
