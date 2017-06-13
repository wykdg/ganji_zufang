import requests


def proxy_check(proxy):
    proxy_check_url = "http://gz.58.com/"
    # ip_check, port_check,=proxy
    try:

        proxy_ip = {'http': "http://%s"%(proxy,)}
        # print proxy_ip
        html2 = requests.get(url=proxy_check_url,proxies=proxy_ip,timeout=3)
        # print html2
        if html2.status_code == 200  :
            print 'add_ip:',proxy
            return True
        return False

    except Exception,e:
        pass
        print e.message


if __name__=='__main__':
    for line in open('s5xu.txt').readlines():
        item = line.strip().split('----')
        proxy_check(item)