# coding=utf-8
import datetime
import json
import os
import re
import tempfile
import time
import vvv8
import requests
import random
import re
from lxml import etree


class Login_58:
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
        elif len(proxy)==2:
            self.proxy = {
                'http': "http://%s:%s" % (proxy[0], proxy[1]),
                'https': "http://%s:%s" % (proxy[0], proxy[1]),
            }
        else:
            self.proxy = {
                'http': "http://%s" % (proxy,),
                'https': "http://%s" % (proxy,),
            }
        url='https://passport.58.com/login/showlogin'
        g=self.fetch(url,params={
            'divid':'userPwdLogin',
            'path':'http://my.58.com/?pts='+self.get_unix_time(),
            'showremmberpwd':'true',
            'viewname':'indexlogin',
            'callback':'usernameLoginSucc',
            'source':'pc-login',
            'originsource':'passport'

        })
        form=re.findall("var domStr = '(.*)';",g.text)
        try:
            html=etree.HTML(form[0])
            m=html.xpath('//input[@id="rsaModulus"]/@value')[0]
            e = html.xpath('//input[@id="rsaExponent"]/@value')[0]
            print 1
        except:
            e = '010001'
            m = '008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f'

        self.encrypt=vvv8.Enerypt_58(e,m)

    @staticmethod
    def get_unix_time():
        dtime = datetime.datetime.now()
        ans_time = time.mktime(dtime.timetuple())
        return str(int(ans_time))+'123'

    @staticmethod
    def get_random():
        str(random.random())

    def fetch(self, url, data=None, **kw):
        if data is None:
            func = self.session.get
        else:
            kw['data'] = data
            func = self.session.post
        if kw.get('headers') is None:
            kw['headers'] = {}
        kw['headers']['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        if kw.get('allow_redirects') is not True:
            kw['allow_redirects'] = False
        else:
            kw['allow_redirects'] = True

        return func(url, proxies=self.proxy, verify=False, timeout=10,  **kw)

    session = requests.Session()

    def login(self, captcha=False):


        header={

            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Referer": "https://passport.58.com/login/?path=http%3A//gz.58.com/&PGTID=0d100000-0000-3dec-4618-0e089c36f8a9&ClickID=1",

        }
        callback = "successFun"
        login_url = "https://passport.58.com/login/dologin"
        g = self.fetch(login_url, data={
            "btnSubmit":u'登录中...',
            "callback": 'successFun',
            "finger2": 'zh-CN|24|1|4|1920_1080|1920_1040|-480|1|1|1|undefined|1|unknown|Win32|unknown|4|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|49bb1579d23252199dec659363649816',
            "fingerprint": 'C739825CA2D1F5FE711104C3FA4A6B34C72BDA83D237A230_011',
            "isremember": 'false',
            "password":self.encrypt.energy(self.get_unix_time()+self.pwd),
            "path": "http://gz.58.com/?pts="+self.get_unix_time(),
            "source": "pc-login",
            "timesign": '',
            "tokenId": '1352710909',
            'username': self.user,
            'validcode': '',
            'vcodekey': '',
            'yzmstate': '',
        },headers=header)
        result = json.loads(re.findall(callback+'\((.*)\)',g.text)[0])
        back={
            "code":0,
            "msg":u''
        }
        if result["msg"] == u'成功':
            print u"登录成功"
            # return True
        elif result["msg"]==u"该用户名与密码不符":
            print u"密码错误"
            back["code"]=1
            # return u"密码错误"
        elif u"验证码" in result["msg"]:
            print u"验证码错误"
            back["code"]=2
            # return u"验证码错误"
        else:
            print result["msg"]
            # return  result["msg"]
            back["code"]=3
        back["msg"]=result["msg"]
        return back
    def get_auth(self):
        url='http://authcenter.58.com/authcenter/authListPage/getAuthListPageInfo'
        g=self.fetch(url)
        data=json.loads(g.text)
        result={}
        if data['code']==1:
            for key,item in data['authType'].items():
                result[int(key)]=item['authState']!="-1"
            return result
        else:
            return None


    def get_jiaoyibao(self):
        url='http://paycenter.58.com/balance?transType=0&r=0.6739341339783008'
        g=self.fetch(url).text
        root=etree.HTML(g)
        ky=root.xpath('//span[@class="ky"]/text()')
        if ky:
            return ky[0]
        else:
            return False

    def get_yue(self):
        url='http://paycenter.58.com/balance?transType=1&r=0.8890172978755696'
        g=self.fetch(url).text
        root=etree.HTML(g)
        ky=root.xpath('//span[@class="ky"]/text()')
        if ky:
            return ky[0]
        else:
            return False

    def get_tuiguang(self):
        url='http://paycenter.58.com/mybid?r=0.3800706547264824'
        g=self.fetch(url).text
        root=etree.HTML(g)
        ky=root.xpath('//span[@class="ky"]/text()')
        if ky:
            return ky[0]
        else:
            return False

    def get_money(self):
        return self.get_jiaoyibao(),self.get_yue(),self.get_tuiguang()

    def modify_password(self,new_pwd):
        url="https://passport.58.com/uimodifypassword/modify"
        header={
            'Referer': 'http://my.58.com/password/?sys=my&pts='+self.get_unix_time()+'&r=0.1475907263100179'
        }
        g = self.fetch(url, data={
            "callback": 'submitcallback',
            'oldpwd':self.pwd,
            'newpwd':new_pwd,
            'renewpwd': new_pwd
        },headers=header,allow_redirects=True)
        callback='submitcallback'
        result = json.loads(re.findall(callback + '\((.*)\)', g.text)[0])
        print result['msg']
        code=result['code']
        if code ==0:
            self.pwd=new_pwd

            return True
        else:
            return result['msg']

if __name__ == "__main__":
    proxy=["127.0.0.1","8888"]
    a = Login_58("15902084922", "58wyk123", proxy)
    if a.login()["code"] is 0:
        a.get_auth()
        print a.get_money()
        # a.modify_password('58wyk12345')