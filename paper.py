# coding: utf-8
import json
import requests
import sys
import urllib.parse
import urllib3

def get_json(id):
    url = 'https://imsummer.cn/api/v3/papers/'+id
    headers = {
        'Host':'imsummer.cn', 
        'Content-Type':'application/json', 
        'Connection':'keep-alive', 
        'platform':'ios' ,
        'Accept':'*/*', 
        'version':'2.1.2', 
        'User-Agent':'Summer/2.1.2 (iPhone; iOS 10.3.3; Scale/2.00)',
        'Accept-Language':'zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8',
        'Authorization':'xxx',
        'Accept-Encoding':'gzip, deflate'
    }
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    r = requests.get(url, headers=headers, timeout=1, verify=False)
    r.encoding='utf-8'
    file = open(id+".json",'ab')
    a = str(r.text)
    if a == "[]" :
        file.close()
        return 0
    else:
        a = a.encode("UTF-8","ignore")
        file.write(a)
        #print("ok")
        file.close()
        return 1

if __name__ == '__main__':
    # 禁用安全请求警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    paperid="xxx"
    get_json(paperid)
    print("Done!")
