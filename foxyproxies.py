from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
import json
from random import randint
random1 = str(randint(0, 50000000000))
def get_proxies(good):
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for g in good:
        proxies.add(g)
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[5][contains(text(),"elite proxy")]') and (i.xpath('.//td[3][contains(text(),"US")]') or i.xpath('.//td[3][contains(text(),"CA")]') or i.xpath('.//td[3][contains(text(),"UK")]')or i.xpath('.//td[3][contains(text(),"DE")]') or i.xpath('.//td[3][contains(text(),"FR")]')) :
            print(i.xpath(".//td[3]/text()"))
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


#If you are copy pasting proxy ips, put in the list below
#proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
import time
good = []
while True:
    proxies = get_proxies(good)
    print(len(proxies))
    good = []
    proxy_pool = cycle(proxies)
    url = 'https://httpbin.org/ip'
    proxySettings = []
    for i in range(1,len(proxies) - 1):
        #Get a proxy from the pool  
        proxy = next(proxy_pool)
        print("Request #%d"%i)
        try:
            response = requests.get(url,proxies={"http": proxy, "https": proxy})

            good.append(proxy)
            
            
            with open('c:\\wamp64\\www\\foxy.PAC', 'w') as f:
                str = '["'
                for g in good:
                    str = str + 'PROXY ' + g + '","'
                str = str[:-2] + ']'
                print(str)
                f.write('function FindProxyForURL(url, host) {\nvar proxies = ' + str + ';\n\nreturn proxies[getRandomInt(0, proxies.length - 1)];\n }\n\n function getRandomInt(firstIndex, lastIndex) {\nreturn firstIndex + (Math.floor((lastIndex - firstIndex + 1) * Math.random()));\n}')
        except Exception as e:
            a = 1
      
print(good)
