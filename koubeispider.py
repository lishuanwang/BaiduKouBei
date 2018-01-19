# coding=utf-8

import urllib2
import re
from lxml import etree


class Spider(object):
    """
        百度口碑（达内集团）爬虫类
    """
    def __init__(self):
        self.url = "https://koubei.baidu.com/s/76e0eb471cf9bd323fb1dc1717a2d451?tab=comt&page="

        self.beginpage = int(raw_input("请输入你的起始页码："))

        self.endpage = int(raw_input("请输入您的终止页码："))

        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

        self.offset = 0

    def koubeiSpider(self):
        """
           获取每一条评论的网页
        """
        for page in range(self.beginpage, self.endpage+1):
        
            url = self.url + str(page)

            req = urllib2.Request(url, headers=self.ua_header)

            response = urllib2.urlopen(req)

            html = response.read()

            selector = etree.HTML(html)

            com_urls = selector.xpath("//div[@class='kb-comt-detail']/a/@href")

            for com_url in com_urls:

                full_url = 'https://koubei.baidu.com'+com_url

                self.loadPage(full_url)

    def loadPage(self, url):
        req = urllib2.Request(url, headers=self.ua_header)

        response = urllib2.urlopen(req)

        html = response.read()

        self.handleHtml(html)

    def handleHtml(self, html):

        selector=etree.HTML(html)

        item_list = selector.xpath("//div[@class='kb-comt-detail']//pre/text()")

        for item in item_list:

            self.writeHtml(item)

    def writeHtml(self, item):

        self.offset += 1

        print ('正在保存第'+str(self.offset)+'条')

        filename = open('./koubei.txt', 'a')

        filename.write(str(self.offset) + item.encode("utf8")+'\n\n')
                
        filename.close()

        print "保存完毕"
if __name__ == '__main__':

    mySpider = Spider()
    mySpider.koubeiSpider()