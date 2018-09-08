#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests


def main():
    url = "http://ic.qq.com/pim/contact/card/search_by_key_json.jsp"
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "150",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "t_user_agent=A54EB83090ED984332F4ECA22D3EC5E4; loginIntroImg=1; SESSION_JSESSIONID=1ef83191-2388-49d9-ad1f-a8dcd5a56455; Hm_lvt_58073b66237937cdd3f99ecdeab79ef3=1533260456; pgv_pvi=8828621824; pgv_si=s321475584; _qpsvr_localtk=0.11098009298025091; pt2gguin=o0794564669; uin=o0794564669; skey=@t38g5Dwr5; ptisp=cnc; RK=SGR1ceIlaD; ptcz=caae6078893b7bedf3f5c4442b0eba6075198031ad432a25e8e54efde9df299f; Hm_lpvt_58073b66237937cdd3f99ecdeab79ef3=1533260915",
        "origin": "https://ic.qq.com",
        "referer": "https://ic.qq.com/pim/contact.jsp",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    response = requests.post(url=url, headers=headers)
    print(response)
    print(response.text)


if __name__ == '__main__':
    main()
