#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import redis


def main():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    # 提取1到100页的url
    for page in range(1):
        next_url = "https://www.liepin.com/zhaopin/?&key=python&curPage={}".format(page)
        r.lpush("liepin:start_urls", next_url)


if __name__ == '__main__':
    main()
