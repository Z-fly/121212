# -*- coding: utf-8 -*-

BOT_NAME = 'manhua'
SPIDER_MODULES = ['manhua.spiders']
NEWSPIDER_MODULE = 'manhua.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'manhua.pipelines.ManhuaPipeline': 1,
}
IMAGES_STORE = 'F:/桌面/漫画'
DOWNLOAD_DELAY = 0.25
