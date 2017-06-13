# -*- coding: utf-8 -*-
import scrapy
from xiaoqu.items import XiaoquItem
import json
import re

class XiaoQuNameSpider(scrapy.Spider):
    name = "xiao_qu_name"
    allowed_domains = ["ganji.com"]

    def __init__(self, city='gz', *args, **kwargs):
        self.start_urls=['http://www.ganji.com/index.htm']
        # self.city=city
        # self.start_urls = ['http://%s.ganji.com/xiaoquzufang/' % (city,)]

        super(XiaoQuNameSpider, self).__init__(*args, **kwargs)
    def parse(self, response):
        urls=response.xpath('//div[@class="all-city"]/dl/dd/a/@href').extract()
        for url in urls:
            url+='xiaoquzufang/'
            city=re.findall('http://(.*?)\.ganji.com',url)[0]
            meta={
                'city':city
            }
            yield scrapy.Request(url=url,meta=meta,callback=self.parse_city)

    def parse_city(self, response):
        auto_complete_url = "http://www.ganji.com/ajax.php"
        for item in response.xpath('//a[@class="list-info-title"]/text()').extract():
        #     data=XiaoquItem()
        #     data['name']=item
            params = {
                "_pdt": "fang",
                "module": "xiaoqu_name_autocomplete",
                "key": item,
                "city": response.meta['city']
            }
            url_params='?'+'&'.join([key+'='+value for key,value in params.items()])
            yield scrapy.Request(url=auto_complete_url+url_params,callback=self.parse_auto_complete,meta=response.meta)
        next=response.xpath('//a[@class="next"]/@href')
        if next:

            url=response.urljoin(next[0].extract())
            yield scrapy.Request(url=url,callback=self.parse_city,meta=response.meta)

    def parse_auto_complete(self, response):
        if response.text:
            url = "http://www.ganji.com/ajax.php?_pdt=fang&module=XiaoquGetInfoByIdV2"
            for item in json.loads(response.text):

                data = {
                    "name": str(item['x_id']),
                    "xiaoqu": item['name'],
                    "domain": response.meta['city']

                }
                yield scrapy.FormRequest(url,method="POST",formdata=data,callback=self.parse_address,meta=response.meta)

    def parse_address(self, response):
        if response.text!='null':
            result=json.loads(response.text)
            data=XiaoquItem()
            # print result['district_info']['name'], result['district_info']['id'], result['street_info']['name'], \
            # result['street_info']['id'], result['address']
            data['name'] = result['name']
            data['address']  =  result['address']
            if result.get('district_info'):
                data['region_name']  = result['district_info'].get('name')
                data['region_id']  =result['district_info'].get('id')
            else:
                data['region_name'] = None
                data['region_id']=None
            if result.get('street_info'):
                data['street_name']  = result['street_info'].get('name')
                data['street_id']  =result['street_info'].get('id')
            else:
                data['street_name'] = None
                data['street_id']=None
            # data['street_name']  = None
            #
            # data['street_id']  = result['street_info'].get('id')
            data['id']=result['id']
            data['city']=result['city']
            yield data
    # def parse_auto_complete(self, response):
        # response = requests.post(url, data=data)
        # if response.status_code == 200 and response.text:
        #     return json.loads(response.text)

    #
    # def get_auto_complete(city,key):
    #     url="http://www.ganji.com/ajax.php"
    #     params={
    #         "_pdt":"fang",
    #         "module":"xiaoqu_name_autocomplete",
    #         "key":key,
    #         "city":self.city
    #     }
    #     response=requests.get(url,params=params)
    #     if response.status_code == 200 and response.text:
    #         return json.loads(response.text)
    #     else:
    #         return []
    #
    #
    # def get_address(name, xiaoqu,domain):
    #     url = "http://www.ganji.com/ajax.php?_pdt=fang&module=XiaoquGetInfoByIdV2"
    #     data = {
    #         "name": name,
    #         "xiaoqu": xiaoqu,
    #         "domain": domain,
    #
    #     }
    #     response = requests.post(url, data=data)
    #     if response.status_code == 200 and response.text:
    #         return json.loads(response.text)
    #     else:
    #         return None