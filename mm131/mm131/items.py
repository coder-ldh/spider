# -*- coding: utf-8 -*-

import scrapy


class Item(scrapy.Item):
    #标题
    image_title = scrapy.Field()
     #图片Id
    image_id = scrapy.Field()
    #来自哪里
    image_from = scrapy.Field()
    #创建时间
    create_time = scrapy.Field()
    #图片路径入口
    image_href = scrapy.Field()
    #图片路径
    image_url = scrapy.Field()
    #图片名称
    image_name = scrapy.Field()
    #页码总数
    image_num = scrapy.Field()
    #分类编号
    category_code = scrapy.Field()
    #分类Id
    category_id = scrapy.Field()
    #存储的目录
    path = scrapy.Field()