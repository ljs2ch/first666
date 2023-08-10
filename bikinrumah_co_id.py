







from lxml import html,etree


import requests

cookies = {
    '_gcl_au': '1.1.2214926.1691637877',
    '_ga': 'GA1.1.910846254.1691637878',
    '_ga_WRDJ0PPHJF': 'GS1.1.1691661202.5.0.1691661342.0.0.0',
}

headers = {
    'authority': 'bikinrumah.co.id',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_gcl_au=1.1.2214926.1691637877; _ga=GA1.1.910846254.1691637878; _ga_WRDJ0PPHJF=GS1.1.1691661202.5.0.1691661342.0.0.0',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

response = requests.get('https://bikinrumah.co.id/', cookies=cookies, headers=headers)

print(response.text)


html=etree.HTML(response.text)

html.xpath('/html/body/div[2]')

import json
import re
import time
from multiprocessing.dummy import Pool
from curl_cffi import requests
from lxml import html,etree
from lxml.etree import HTMLParser

class  He_Ni:
    def __init__(self):
        self.cookies = {
    'pll_language': 'id',
    '_gcl_au': '1.1.546543933.1691635278',
    '_gid': 'GA1.2.1793623400.1691635278',
    '_tt_enable_cookie': '1',
    '_ttp': 'FEpct2X2MOfGKhKLUo9YqLaLb2T',
    '_ga': 'GA1.1.92918592.1691635278',
    '_gat_gtag_UA_205128313_1': '1',
    '_ga_0N4TW5QW2F': 'GS1.1.1691635277.1.1.1691635448.0.0.0',
    '_ga_LTVMKQ652R': 'GS1.1.1691635277.1.1.1691635448.0.0.0',
}
        self.headers = {
    'authority': 'hewania.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'pll_language=id; _gcl_au=1.1.546543933.1691635278; _gid=GA1.2.1793623400.1691635278; _tt_enable_cookie=1; _ttp=FEpct2X2MOfGKhKLUo9YqLaLb2T; _ga=GA1.1.92918592.1691635278; _gat_gtag_UA_205128313_1=1; _ga_0N4TW5QW2F=GS1.1.1691635277.1.1.1691635448.0.0.0; _ga_LTVMKQ652R=GS1.1.1691635277.1.1.1691635448.0.0.0',
    'pragma': 'no-cache',
    'referer': 'https://hewania.com/blog/page/3/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

    def get_text(self,url):
        '''
        :param
        获取 整体的数据
        :return:
        '''

        response = requests.get(url, cookies=self.cookies, headers=self.headers)

        return response.text

    # class ="btContent"
    def parse(self):
        '''
        :param
        数据提取
        使用列表的形式存储链接
        :return:
        '''
        try:
            news_links = []
            url = 'https://hewania.com/blog/page/{}/'.format(str(1))
            data = self.get_text(url)
            html = etree.HTML(data)
            aside = html.xpath('//*[@id="top"]/div[2]/div[2]/aside/div[2]/div/ul/li')
            for s in aside:
                new_link = s.xpath('./div/div[2]/header/h4/span/span/a/@href')[0]
                news_links.append(new_link)
            # print(news_links)
            page=1
            while True:
                url='https://hewania.com/blog/page/{}/'.format(str(page))
                data=self.get_text(url)
                # print(data)
                if "error404"   in data:
                    break
                else:

                    html_data = re.findall('''<div class="btContent">(.*?)<aside class="btSidebar">''', data, re.S)[0]
                    news_link = re.findall('''</span><a href="(.*?)"''', html_data, re.S)
                    # print(news_link)
                    for i in news_link:
                        news_links.append(i)

                    page += 1


            #  对数据进行去重
            news_links = [x for i, x in enumerate(news_links) if x not in news_links[:i]]
            print(len(news_links),news_links)
            return news_links


        except Exception as e:
                raise  e






    def run(self):
        thead_pool=Pool(32)
        thead_pool(self.parse())
        thead_pool.join()
        thead_pool.close()




if __name__ == '__main__':
    pass
    # start=time.time()
    # hn =He_Ni()
    # hn.run()
    # print('花费的时间：',time.time()-start)





















