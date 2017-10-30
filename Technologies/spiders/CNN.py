# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import Crawler

class CnnSpider(scrapy.Spider):
    name = 'CNN'
    allowed_domains = ['patents.google.com']
        #'www.cnet.com']
    start_urls = \
        ['https://patents.google.com/advanced?q=deep+learning&q=neural+networks&before=priority:19850101&after=priority:19800101']
        #'https://www.cnet.com/news/20-biggest-tech-innovations-of-my-lifetime-that-i-actually-use/']
    #'https://www.cnet.com/news/20-biggest-tech-innovations-of-my-lifetime-that-i-actually-use/',
    # rules = (
    #     Rule(CrawlSpider(allow=(), restrict_css=('.pageWrapper pageContainer current',)),
    #          callback="parse_item",
    #          follow=True),)

    def parse(self, response):
        return response.url
        Technologies = []

        SET_SELECTOR ='.search-app'
        for x in response.CSS(SET_SELECTOR):
            yield {
            'name':x,
        }
        #SET_SELECTOR  = '.contentWrap'
        # for brickset in response.css(SET_SELECTOR):
        #     NAME_SELECTOR = 'ol li ::text'
        #     yield {
        #         'name': brickset,
        #     }
        #     data = brickset.css(NAME_SELECTOR)
        #     with open('TechnologiesExtract_GCN.txt', 'w') as file:
        #         for i in str(data).split('>')  :
        #             Technologies.append(i)
        #             if ":" in i:
        #                 file.write(i)
        #                 file.write('\n')
        # item_links = response.css('.large > .detailsLink::attr(href)').extract()
        # for a in item_links:
        #     yield scrapy.Request(a, callback=self.parse_detail_page)



