# -*- coding: utf-8 -*-
import scrapy

try:
    from scrapy_redis.spiders import RedisSpider
except:
    from LiePinSpider.scrapy_redis.spiders import RedisSpider
from LiePinSpider.items import MyItems


# class LiepinSpider(scrapy.Spider):
class LiepinSpider(RedisSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    redis_key = "liepin:start_urls"
    # start_urls = ['https://www.liepin.com/zhaopin/?&key=python']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer': 'https://www.liepin.com/zhaopin/'
    }

    # def start_requests(self):
    #     # 提取1到100页的url
    #
    #     for page in range(100):
    #         next_url = "https://www.liepin.com/zhaopin/?&key=python&curPage={}".format(page)
    #         yield scrapy.Request(next_url, callback=self.parse_1, headers=self.headers, dont_filter=True)

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer': response.url
        }

        # 爬取一页的url以及交给spider下载并提取详情
        job_list = response.xpath('//ul[@class="sojob-list"]/li')
        for job in job_list:
            url = "".join(job.xpath('div/div/h3/a/@href').extract())
            print("详情页：{}".format(url))
            yield scrapy.Request(url, callback=self.parse_detail, dont_filter=True,
                                 headers=headers)

    def parse_detail(self, response):
        # 公司名字
        company_name = "".join(response.xpath('//div[@class="title-info"]/h3/a/text()').extract())
        # 回应时间
        release_time = "".join(response.xpath('//p[@class="basic-infor"]/time/@title').extract())
        # 薪资
        money = "".join(response.xpath('//p[@class="job-item-title"]/text()').extract_first('').strip())
        # 要求
        qualifications = "+".join(response.xpath('//div[@class="job-qualifications"]/span/text()').extract())
        # 职位描述
        job_descript = "\n".join(
            response.xpath('//div[@class="job-item main-message job-description"]/div/text()').extract()) \
            .replace('\t', '')
        # 部门
        department = " ".join(response.xpath('//div[@class="about-position"]/div[5]/div/ul/li[1]/span/text()|\
                        //div[@class="about-position"]/div[5]/div/ul/li[1]/label/text()').extract())
        # 专业
        major = " ".join(response.xpath('//div[@class="about-position"]/div[5]/div/ul/li[2]/span/text()|\
                        //div[@class="about-position"]/div[5]/div/ul/li[2]/label/text()').extract())
        # 汇报对象
        reportor = " ".join(response.xpath('//div[@class="about-position"]/div[5]/div/ul/li[3]/span/text()|\
                        //div[@class="about-position"]/div[5]/div/ul/li[3]/label/text()').extract())
        # 下属人数
        under_nums = " ".join(response.xpath('//div[@class="about-position"]/div[5]/div/ul/li[4]/span/text()|\
                        //div[@class="about-position"]/div[5]/div/ul/li[4]/label/text()').extract())
        # 工作地点
        place = "".join(response.xpath('//p[@class="basic-infor"]/span/a/text()').extract())
        company_dd = response.xpath('//ul[@class="new-compintro"]/li').extract()
        if len(company_dd) == 3:
            # 公司地点
            company_place = "".join(response.xpath('//ul[@class="new-compintro"]/li[3]/text()').extract())
            # 公司规模
            company_scale = "".join(response.xpath('//ul[@class="new-compintro"]/li[2]/text()').extract())
            # 公司行业
            company_major = "".join(response.xpath('//ul[@class="new-compintro"]/li[1]/text()|//ul[@class="new-compintro"]\
            /li[1]/a/text()').extract()).strip()
        elif len(company_dd) == 2:
            company_place = ""
            # 公司规模
            company_scale = "".join(response.xpath('//ul[@class="new-compintro"]/li[2]/text()').extract())
            # 公司行业
            company_major = "".join(response.xpath('//ul[@class="new-compintro"]/li[1]/text()|//ul[@class="new-compintro"]\
            /li[1]/a/text()').extract()).strip()
        elif len(company_dd) == 1:
            company_place = ""
            company_scale = ""
            # 公司行业
            company_major = "".join(response.xpath('//ul[@class="new-compintro"]/li[1]/text()|//ul[@class="new-compintro"]\
            /li/a/text()').extract()).strip()
        else:
            company_place = ""
            company_scale = ""
            company_major = ""
        # 公司介绍
        company_introduce = "\n".join(response.xpath('//div[@class="info-word"]/text()').extract()).strip()

        myitem = MyItems()
        myitem['company'] = company_name
        myitem['release_time'] = release_time
        myitem['money'] = money
        myitem['qualifications'] = qualifications
        myitem['job_descript'] = job_descript
        myitem['department'] = department
        myitem['major'] = major
        myitem['reportor'] = reportor
        myitem['under_nums'] = under_nums
        myitem['place'] = place
        myitem['company_place'] = company_place
        myitem['company_scale'] = company_scale
        myitem['company_major'] = company_major
        myitem['company_introduce'] = company_introduce
        yield myitem
