# -*- coding:utf-8 -*-
import datetime
import io
import os
import sys

from idna import unicode
from lxml import etree
from check.pymysql_comm import UsingMysql
from check.upload_baidu import fetch_page_data


def generatr_xml_index(filename, sitemap_list):
    """Generate sitemap index xml file."""
    time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    root = etree.Element('sitemapindex')
    for each_sitemap in sitemap_list:
        sitemap = etree.Element('sitemap')
        loc = etree.Element('loc')
        loc.text = each_sitemap
        lastmod = etree.Element('lastmod')
        lastmod.text = time
        sitemap.append(loc)
        sitemap.append(lastmod)
        root.append(sitemap)

    header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    s = etree.tostring(root, encoding='utf-8', pretty_print=True)
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(unicode(header + str(s, encoding="utf-8")))


def file_filter(f):
    if f[-4:] in ['.txt']:
        return True
    else:
        return False


def creat_file(output_path, urls):
    with open(output_path, "w", encoding='utf8') as file:
        try:
            for url in urls:
                file.write(str(url) + '\n')
        except Exception as e:
            print(e)

    file_list = os.listdir("/Users/caichen/PycharmProjects/spider/baidu_upload/check/sitemap")
    file_list = list(filter(file_filter, file_list))
    file_list.reverse()
    new_file_list = []
    for file_name in file_list:
        new_file_list.append("https://www.zhifoubj.com/sitemap/" + file_name)
    generatr_xml_index("/Users/caichen/PycharmProjects/spider/baidu_upload/check/sitemap.xml", new_file_list)


def start():
    n = 1
    total = 0
    with UsingMysql(log_time=True) as um:
        page_size = 100
        originUrls = []
        for page_no in range(1, 10000):
            print('====== 第%d页' % page_no)
            skip = (page_no - 1) * page_size
            data = fetch_page_data(um.cursor, page_size, skip)
            if data.__len__() == 0:
                file_name = "/Users/caichen/PycharmProjects/spider/baidu_upload/check/sitemap/%s.txt" % n
                creat_file(file_name, originUrls)
                sys.exit(0)

            for url in data:
                originUrl = "https://www.zhifoubj.com/articleDetail/" + url["article_id"]
                originUrls.append(originUrl)
                total += 1
                if total == 20000:
                    file_name = "/Users/caichen/PycharmProjects/spider/baidu_upload/check/sitemap/%s.txt" % n
                    creat_file(file_name, originUrls)
                    originUrls.clear()
                    total = 0
                    n += 1


if __name__ == '__main__':
    start()
