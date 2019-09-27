# comic.ikkdm.com
KuKu动漫爬虫

## 运行 
cd manhua  
scrapy crawl comic

## kukudm.py参数设置
.server_img 图片服务器地址，通过浏览器自行修改

.start_urls 漫画本体地址

.is_all 是否下载全部 （True or False）

.start_order_down 下载的起始话

.start_order_up 下载的最后话 （在.is_all = False下启用）

<br>

本地保存目录在settings.py下设置

## 参考资料
https://blog.csdn.net/zyf2333/article/details/84405034
