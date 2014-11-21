import urllib2
import re

def ottobib(isbn):
    fp = urllib2.urlopen("https://www.ottobib.com/isbn/%s/bibtex" % isbn)
    html = fp.read()
    match = re.findall("<textarea .*?>(.*?)</textarea>", html, re.DOTALL)
    if len(match) > 0:
        return match[0]
    raise Exception("ISBN not found")
