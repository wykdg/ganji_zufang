#coding=utf8
import requests
import json
def get_auto_complete(city,key):
    url="http://www.ganji.com/ajax.php"
    params={
        "_pdt":"fang",
        "module":"xiaoqu_name_autocomplete",
        "key":key,
        "city":city
    }
    response=requests.get(url,params=params)
    if response.status_code == 200 and response.text:
        return json.loads(response.text)
    else:
        return []


def get_address(name, xiaoqu,domain):
    url = "http://www.ganji.com/ajax.php?_pdt=fang&module=XiaoquGetInfoByIdV2"
    data = {
        "name": name,
        "xiaoqu": xiaoqu,
        "domain": domain,

    }
    response = requests.post(url, data=data)
    if response.status_code == 200 and response.text:
        return json.loads(response.text)
    else:
        return None



if __name__=='__main__':
    city='zhongshan'
    key=u"夏阳新村"
    for item in  get_auto_complete(city,key):
        print item['name'],item['address'],
        result=get_address(item['x_id'],item['name'],city)
        print result
        print result['district_info']['name'],result['district_info']['id'],result['street_info']['name'],result['street_info']['id'],result['address']