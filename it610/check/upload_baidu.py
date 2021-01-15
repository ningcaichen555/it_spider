import json
import os
import sys

import requests

from check.pymysql_comm import UsingMysql


def push_urls(urls):
    headers = {
        'User-Agent': 'curl/7.12.1',
        'Host': 'data.zz.baidu.com',
        # 'Host': 'data.zhanzhang.sm.cn',
        'Content - Type': 'text / plain',
        'Content - Length': '83'
    }
    try:
        # 将列表进行拼接
        post_data = '\n'.join(urls)
        print(post_data)
        html = requests.post(url="http://data.zz.baidu.com/urls?site=https://www.zhifoubj.com&token=PBVcZiAH8Yf0PktW",
                             headers=headers, data=post_data, timeout=30).content
        # html = requests.post(
        #     url="https://data.zhanzhang.sm.cn/push?site=www.zhifoubj.com&user_name=pfxxzhan@163.com&resource_name=mip_add&token=TI_4c46d2f44c8f3b72ce1152acc355b6dc",
        #     headers=headers, data=post_data, timeout=30).content
        # print(json.loads(html.decode('utf-8')))
        remain = json.loads(html.decode('utf-8')).get("remain")
        if remain > 0:
            print(html)
        else:
            sys.exit(0)
    except Exception as e:
        return "{'error}" + e


def fetch_page_data(cursor, page_size, skip):
    sql = 'select article_id from article limit %d,%d' % (skip, page_size)
    cursor.execute(sql)
    data_list = cursor.fetchall()
    print('-- 数据: {0}'.format(data_list))
    return data_list


def startPushUrl():
    with UsingMysql(log_time=True) as um:
        page_size = 10
        for page_no in range(1, 1000):
            print('====== 第%d页数据' % page_no)
            skip = (page_no - 1) * page_size
            data = fetch_page_data(um.cursor, page_size, skip)
            originUrls = []
            for url in data:
                originUrl = "https://www.zhifoubj.com/articleDetail/" + url["article_id"]
                originUrls.append(originUrl)
            push_urls(originUrls)


def createSitemap():
    path = "sitemap/sitemap0001.txt"
    with open(path, 'w', encoding='utf-8') as f:
        f.write('Hello, python!')


def startCreateSiteMap():
    createSitemap()


if __name__ == '__main__':
    startPushUrl()
    # startCreateSiteMap()
