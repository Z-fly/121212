# -*- coding: utf-8 -*-

import os
import requests
from manhua import settings


class ManhuaPipeline(object):
    @staticmethod
    def process_item(item, spider):
        if 'img_url' in item:
            images = []
            dir_path = '%s/%s' % (settings.IMAGES_STORE, item['dir_name'])
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            page = item['link_url'].split('/')[-1].split('.')[0]
            image_file_name = page.zfill(2) + '.jpg'
            file_path = '%s/%s' % (dir_path, image_file_name)
            images.append(file_path)
            print(item)
            print(file_path)
            with open(file_path, 'wb') as fp:
                response = requests.get(url=item['img_url'])
                for block in response.iter_content(1024):
                    if not block:
                        break
                    fp.write(block)
            item['image_paths'] = images
