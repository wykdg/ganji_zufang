# coding=utf-8
import datetime
import json
import os
import re
import tempfile
import time

import requests


class GanJiLogin:
    def __init__(self, user, pwd, proxy=None, rk_username=None, rk_password=None):
        self.user = user
        self.pwd = pwd
        self.rk_username = rk_username
        self.rk_password = rk_password
        if proxy is None:
            self.proxy = None
        elif len(proxy) == 4:
            self.proxy = {
                'http': "socks5://%s:%s@%s:%s" % (proxy[2], proxy[3], proxy[0], proxy[1]),
                'https': "socks5://%s:%s@%s:%s" % (proxy[2], proxy[3], proxy[0], proxy[1]),
            }
        else:
            self.proxy = {
                'http': "http://%s:%s" % (proxy[0], proxy[1]),
                'https': "http://%s:%s" % (proxy[0], proxy[1]),
            }

    @staticmethod
    def get_unix_time():
        dtime = datetime.datetime.now()
        ans_time = time.mktime(dtime.timetuple())
        return str(int(ans_time))

    def fetch(self, url, data=None, **kw):
        if data is None:
            func = self.session.get
        else:
            kw['data'] = data
            func = self.session.post
        if kw.get('headers') is None:
            kw['headers'] = {}
        kw['headers']['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"

        return func(url, proxies=self.proxy, verify=False, timeout=10, allow_redirects=False, **kw)

    session = requests.Session()

    def login(self, captcha=False):

        login_form_url = "https://passport.ganji.com/login.php?next=/"
        g = self.fetch(login_form_url).text
        hahs_key = re.findall("__hash__ = '(.*?)'", g)[0]

        vcode = self.get_captchas(captcha)

        callback = "jQuery182013097555513186343_1496738863063"
        login_url = "https://passport.ganji.com/login.php"
        g = self.fetch(login_url, params={
            "callback": callback,
            "username": self.user,
            "password": self.pwd,
            "checkCode": vcode,
            "setcookie": 14,
            "parentfunc": "",
            "redirect_in_iframe": "",
            "next": "/",
            "__hash__": hahs_key,
            "_": self.get_unix_time(),

        })
        # print g.text[len(callback):-1]
        result = json.loads(g.text[len(callback) + 1:-1])
        if result["status"] == 1:
            print u"登录成功"
            return True
        elif result.get('type') and result.get('type') == "need_captcha":
            print u"验证码错误"
            return self.login(True)
        else:
            print u"用户名或密码错误"

    def get_captchas(self, need):
        image_url = "https://passport.ganji.com/ajax.php"
        header_img = {

            "Accept": "image/webp,image/*,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
        }
        r = self.fetch(image_url, params={
            "dir": "captcha",
            "module": "login_captcha",
            "nocache": self.get_unix_time()
        }, headers=header_img)
        if need is False:
            return ""
        tmp = tempfile.mkstemp(suffix='.jpg')
        os.write(tmp[0], r.content)
        os.close(tmp[0])
        os.startfile(tmp[1])

        # rc = RClient(self.rk_username, self.rk_password)
        # im = open(tmp[1], 'rb').read()
        # result = rc.rk_create(im, 3040)
        # ans = result['Result']
        # print result['Result']


        ans = raw_input('Verify code: ')

        os.remove(tmp[1])
        return ans


if __name__ == "__main__":
    a = GanJiLogin("15902084922", "ganjiwyk")
    a.login()
