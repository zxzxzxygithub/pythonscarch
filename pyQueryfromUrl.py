from pyquery import PyQuery as pq
doc = pq('https://www.baidu.com')
# doc1 = pq(url='https://www.baidu.com')
print(doc)
print(doc('head'))