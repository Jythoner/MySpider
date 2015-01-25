# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector,HtmlXPathSelector
from MySpider.items import Website
import sys
sys.stdout = open('output.txt', 'w')   #将打印信息输出在相应的位置下


class MySpider(CrawlSpider):

    name = "test"
    allowed_domains = ["the5fire.com"]
    start_urls = [
        "http://www.the5fire.com/",
    ]

    rules = (

        Rule(SgmlLinkExtractor(allow=('\?page=\d+', )),),
        Rule(SgmlLinkExtractor(allow=('.*\.html', )), callback='parse_item'),

    )

    def parse_item(self, response):
        self.log("This is a page : %s " % response.url)
        sel = Selector(response)

        item = Website()
        item['Title'] = sel.xpath('//h2[@class="under_line"]/span/text()').extract()[0] #观察网页对应得html源码
        item['url'] = response.url
        print 'title :  ' +  item['Title']
        print 'url :  ' + item['url']

        return item
