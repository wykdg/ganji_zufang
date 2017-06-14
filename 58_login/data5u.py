# -*- coding: UTF-8 -*-

'''
无忧代理IP Created on 2016年12月23日
@author: www.data5u.com
'''

import urllib
import random

if __name__ == '__main__':
    # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
    order = "888888888888888";
    # 获取IP的API接口
    apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order;
    # 要抓取的目标网站地址


    try:
        # 获取IP列表
        # res = urllib.urlopen(apiUrl).read().strip("\n");
        # 按照\n分割获取到的IP
        # ips = res.split("\n");
        # 随机选择一个IP
        # proxyip = random.choice(ips)
        targetUrl = "http://1212.ip138.com/ic.asp";
        # 使用代理IP请求目标网址
        html = urllib.urlopen(targetUrl)
        # 输出内容
        print(" 获取到如下HTML内容：\n" + unicode(html.read(), "gb2312").encode("utf8"))
    except Exception, e:
        print(e)