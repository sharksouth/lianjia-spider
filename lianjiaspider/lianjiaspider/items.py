# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewhouseItem(scrapy.Item):        #新房

    loupan = scrapy.Field()         #楼盘
    types = scrapy.Field()          #类型      别墅、商业类....
    location =scrapy.Field()        #位置
    rooms =scrapy.Field()           #房型      3室、4室
    price_per_m2 = scrapy.Field()   #单价
    price_all =scrapy.Field()       #总价
    area = scrapy.Field()           #面积


class OldhouseItem(scrapy.Item):        #二手房

    estate = scrapy.Field()         #小区
    types = scrapy.Field()          #类型      别墅、商业类....
    location =scrapy.Field()        #位置
    rooms =scrapy.Field()           #房型      3室、4室
    price_per_m2 = scrapy.Field()   #单价
    price_all =scrapy.Field()       #总价
    area = scrapy.Field()           #面积
    info = scrapy.Field()

