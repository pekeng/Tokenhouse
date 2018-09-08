# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class LiepinspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MyliepinPipelines(object):
    # 连接数据库
    def __init__(self):
        self.connect = pymysql.connect(host='192.168.0.126',
                                       port=3306,
                                       user='root',
                                       password='rootpasswd',
                                       database='jianjian',
                                       charset='utf8'
                                       )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        insert_sql = 'insert into ss(company,release_time,\
                      money,qualifications,job_descript,department,\
                      major,reportor,under_nums,place,company_place,\
                      company_scale,company_major,company_introduce)\
                      value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(insert_sql,(item['company'] ,item['release_time'] \
                                                ,item['money'] ,item['qualifications'] ,item['job_descript'] \
                                                ,item['department'] ,item['major'] ,item['reportor'] \
                                                ,item['under_nums'] ,item['place'] ,item['company_place'] \
                                                ,item['company_scale'] ,item['company_major'] \
                                                ,item['company_introduce']))
            self.connect.commit()
        except Exception as e:
            print(e)
            self.connect.rollback()
        return item
