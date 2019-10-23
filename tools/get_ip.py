import requests
import random
import re
from lxml import etree


def get_ip():
    headers_list = [
        {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
        {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
        {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'},
    ]
    ip_list = []
    for x in range(1,3):
        headers = random.choice(headers_list)
        url = 'https://www.xicidaili.com/nn/1'
        res = requests.get(url,headers=headers)
        res.encoding = 'utf-8'
        wenben = etree.HTML(res.text)
        vlist = wenben.xpath('//table[@id="ip_list"]//tr[position()>1]')
        for v in vlist:
            make_ip = v.xpath('string(.)').replace('\n','-').replace(' ','')
            ip_s = re.findall('-(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})-(\d{1,6}).*?([A-Z]{4,5})',make_ip)[0]
            'http://ip:端口号'
            ip_txt = '{}://{}:{}'.format(ip_s[2],ip_s[0],ip_s[1])
            ip_list.append(ip_txt)
        print('已爬取完第%d页'%x)
    with open(r'D:\bija_spider\Record\xc_ip.txt', 'w', encoding='utf8') as f:
        for i in ip_list:
            f.write(i+'\n')
    print('写入完成')

if __name__ == "__main__":
    get_ip()