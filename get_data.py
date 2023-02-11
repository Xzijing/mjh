import time

import random

import requests

from bs4 import BeautifulSoup
cookies='ll="108090"; ap_v=0,6.0; __utma=30149280.56995933.1676001084.1676001084.1676001084.1; __utmb=30149280.0.10.1676001084; __utmc=30149280; __utmz=30149280.1676001084.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); __gads=ID=e90d8ee72bb9315c-22eae3b8f4da00e3:T=1676001088:RT=1676001088:S=ALNI_MY6iG-mU9OJlODoobgPfyDvfPIlGw; __gpi=UID=000009a659688527:T=1676001088:RT=1676001088:S=ALNI_MYf5rkO9b29qoBs6wSs0hoCyoj6PQ; dbcl2="157320615:sWDDxWj/Jho"; ck=xi92; push_noty_num=0; push_doumail_num=0'
def get_info(url):

    dict = {}

    UA = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
        ]
    user_agent = random.choice(UA)

    #请求页面
    r = requests.get(url,headers={'User-Agent':user_agent,'cookie':cookies})

    #创建BeautifulSoup对象
    soup = BeautifulSoup(r.text,'lxml')
    
    #找到所有的class属性为comment-item的标签
    comment_items = soup.select('.comment-item')

    #遍历所有符合要求的标签
    for comment_item in comment_items:

        #找到包含短评内容的标签
        shorts = comment_item.select('.short')

        #找到包含时间的标签
        times = comment_item.select('.comment-time')

        #遍历找到的标签
        for short,time in zip(shorts,times):

            #提取文字
            short_text = short.get_text()

            #提取时间
            time_num = time['title']

            #把文字保存下来#使用前先创建一个txt文件
            with open('mjh2.txt','a+',encoding='utf-8') as f:

                f.write(short_text + '\n')

            #print(short_text,time_num)

            dict = {
                'short':short_text,

                'time':time_num
                }

    return dict

if __name__ == '__main__':

    #生成大量的url链接
    urls = ['https://movie.douban.com/subject/35766491/comments?start={}&limit=20&status=P&sort=new_score'.format(str(i)) for i in range(800,100000,20)]

    for url in urls:
        print(url)
        get_info(url)
        time.sleep(5)

        
    