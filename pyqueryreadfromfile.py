from pyquery import PyQuery as pq
doc = pq(filename='aaa.html')
items = doc('.item3line1').items()
for item in items:
    print item
