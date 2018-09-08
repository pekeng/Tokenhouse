# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MyItems(scrapy.Item):
    company = scrapy.Field()
    release_time = scrapy.Field()
    money = scrapy.Field()
    qualifications = scrapy.Field()
    job_descript = scrapy.Field()
    department = scrapy.Field()
    major = scrapy.Field()
    reportor = scrapy.Field()
    under_nums = scrapy.Field()
    place = scrapy.Field()
    company_place = scrapy.Field()
    company_scale = scrapy.Field()
    company_major = scrapy.Field()
    company_introduce = scrapy.Field()
