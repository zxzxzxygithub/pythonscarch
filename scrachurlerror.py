import urllib2

req = urllib2.Request('http://www.lixxxxxxxx.com')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError as e:
    print e.code
    print ('we can not fulfill the request \n')
except urllib2.URLError as e:
    print e.reason
    print 'we can not reach a server'
else:
    print('No problem')
