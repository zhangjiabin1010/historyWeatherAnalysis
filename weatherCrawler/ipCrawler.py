# -*- coding: utf-8 -*-
import requests
from lxml import etree


# 抓取代理
class CrawlProxy(object):
    def crawl_run(self):
        proxies = self.parse_tool() + self.parse_ydl() + self.parse_kdl()
        return proxies

    # @retry(stop_max_attempt_number=5)
    def request_page(self, url):
        # ua = random.choice(WINUA)
        ua = 'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0'
        headers = {'User-Agent': ua}
        response = requests.get(url=url, headers=headers)
        return response

    def parse_kdl(self):
        proxies = []
        for p in [1, 2]:
            for i in ['inha', 'intr']:
                url = f'https://www.kuaidaili.com/free/{i}/{p}/'
                response = self.request_page(url=url)
                tree = etree.HTML(response.text)
                uls = tree.xpath('.//table/tbody/tr')
                for items in uls:
                    ip = items.xpath('./td[@data-title="IP"]/text()')[0]
                    port = items.xpath('./td[@data-title="PORT"]/text()')[0]
                    proxy = ':'.join([ip, port])
                    proxies.append(str(proxy))
        return proxies

def checkProxy(proxy):
    try:
        html = requests.get('http://'+proxy,timeout=5)
        if html.status_code == 200:
            print(proxy)
            return proxy
    except Exception as e:  # 捕获除与程序退出sys.exit()相关之外的所有异常
        print(e)


if __name__ == '__main__':
    CrawlProxy = CrawlProxy()
    ipList = CrawlProxy.parse_kdl()
    for proxy in ipList:
        checkProxy(proxy)
