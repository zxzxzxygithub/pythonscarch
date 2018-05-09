import urllib2

url = 'http://originalix.github.io/#blog'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/64.0.3282.140 Safari/537.36'
headers = {'User-Agent': user_agent}
request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)
html = response.read()
print html