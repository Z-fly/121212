# -*- coding: utf-8 -*-

import scrapy


class ManhuaItem(scrapy.Item):
    dir_name = scrapy.Field()
    link_url = scrapy.Field()
    img_url = scrapy.Field()
    image_paths = scrapy.Field()
    manhua_name = scrapy.Field()
    manhua_link = scrapy.Field()
    dir_name2 = scrapy.Field()
    link_url2 = scrapy.Field()
    img_url2 = scrapy.Field()
    next_page_url = scrapy.Field()
