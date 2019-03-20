# -*- coding: utf-8 -*-
import scrapy
import re

from story_test.items import StoryTestItem 

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.23us.so']
    # sstart_urls = ['https://read.qidian.com/chapter/tcH3TasLtZc6Q5WO_IQttQ2/LUOcipI6gWaaGfXRMrUjdw2']

    def start_requests(self):
        yield scrapy.Request('https://www.23us.so/files/article/html/14/14038/5750080.html',callback=self.parse)

    def parse(self, response):
        item = StoryTestItem()
        item['text'] = response.xpath('//dd[@id="contents"]//text()').extract()
        item['h'] = response.xpath('//meta[@name="keywords"]/@content').extract()[0]
        hr = response.xpath('//dd[@id="footlink"]/a/@href').extract()[2]
        url = f'https://www.23us.so/{hr}'
        yield item
        yield scrapy.Request(url,callback=self.parse)


 
        
    


