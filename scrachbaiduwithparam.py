import urllib
import urllib2

url = 'http://www.baidu.com/'
params = {'name': 'Lix', 'location': 'China'}
data = urllib.urlencode(params)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

print the_page
