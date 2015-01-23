# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from MySpider.items import Website
import sys
sys.stdout = open('we.txt', 'w')   #将打印信息输出在相应的位置下


class MySpider(CrawlSpider):

    name = "test"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/cacique",
    ]

    rules = (

        Rule(SgmlLinkExtractor(allow=('cacique/default\.html\?page=\d+', )), ),
        Rule(SgmlLinkExtractor(allow=('cacique/p/', )), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=('cacique/archive/', )), callback='parse_item'),

    )

    def parse_item(self, response):
        self.log("This is a page : %s " % response.url)
        sel = Selector(response)
        items = []
        item = Website()
        item['headTitle'] = sel.xpath('/html/head/title/text()').extract()[0].encode('utf-8')  #观察网页对应得html源码
        item['url'] = response.url
        print 'title :  ' +  item['headTitle']
        print 'url :  ' + item['url']
        items.append(item)
