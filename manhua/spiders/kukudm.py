# -*- coding: utf-8 -*-

import re

import scrapy
from scrapy import Selector

from manhua.items import ManhuaItem


class KukudmSpider(scrapy.Spider):
    name = 'comic'

    def __init__(self):
        self.server_img = 'http://n9.1whour.com/'
        self.server_link = 'http://comic.ikkdm.com'
        self.allowed_domains = ['comic.ikkdm.com']
        self.start_urls = ['http://comic.ikkdm.com/comiclist/2793/index.htm']
        self.is_all = False
        self.start_order_down = 1
        self.start_order_up = 2
        self.pattern_img = re.compile(r'\+"(.+)\'></a')

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse1)

    def parse1(self, response):
        hxs = Selector(response)
        urls = response.xpath('//dd/a[1]/@href').extract()
        dir_names = response.xpath('//dd/a[1]/text()').extract()
        for index in range(len(urls)):
            # if dir_names[index].split(' ')[1][-1:] != '话':
            #     if input(dir_names[index].split(' ')[1] + '是否忽略(y or n)') == 'y':
            #         continue
            if (float(dir_names[index].split(' ')[1][:-1]) >= self.start_order_down and float(
                    dir_names[index].split(' ')[1][:-1]) <= self.start_order_up) or self.is_all:
                item = ManhuaItem()
                item['link_url'] = self.server_link + urls[index]
                item['dir_name'] = dir_names[index]
                yield scrapy.Request(url=item['link_url'], meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        print(item)
        item['link_url'] = response.url
        print(item)
        hxs = Selector(response)
        pre_img_url = hxs.xpath('//script/text()').extract()
        img_url = (self.server_img + re.search(self.pattern_img, pre_img_url[0]).group(1))
        item['img_url'] = img_url
        yield item
        page_num = hxs.xpath('//td[@valign="top"]/text()').re(u'共(\d+)页')[0]
        pre_link = item['link_url'][:-5]
        for each_link in range(2, int(page_num) + 1):
            new_link = pre_link + str(each_link) + '.htm'
            yield scrapy.Request(url=new_link, meta={'item': item}, callback=self.parse3)

    def parse3(self, response):
        item = response.meta['item']
        item['link_url'] = response.url
        hxs = Selector(response)
        pre_img_url = hxs.xpath('//script/text()').extract()
        img_url = (self.server_img + re.search(self.pattern_img, pre_img_url[0]).group(1))
        item['img_url'] = img_url
        yield item
