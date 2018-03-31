# coding: utf-8
import json
import requests
import sys
import urllib.parse
import urllib3


def get_json(id,limit,offset):
    url = 'https://imsummer.cn/api/v3/user/nearbies'
    payload = {
        'lat':'xxx',
        'limit':limit ,
        'lng':'xxx',
        'offset': offset ,
        'q[school_id_eq]': id , 
        'scope':'global'
    }
    headers = {
        'Host':'imsummer.cn', 
        'Content-Type':'application/json', 
        'Connection':'keep-alive', 
        'platform':'ios' ,
        'Accept':'*/*', 
        'version':'2.2.0', 
        'User-Agent':'Summer/2.2.0 (iPhone; iOS 10.3.3; Scale/2.00)',
        'Accept-Language':'zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8',
        'Authorization':'xxxxxxxxxxxx',
        'Accept-Encoding':'gzip, deflate'
    }
    r = requests.get(url, params=payload, headers=headers, verify=False)
    r.encoding='utf-8'
    
    if r.text == "[]" :
        return 0
    else:
        file = open(id+"-"+str(offset)+".json",'wb')
        a = r.text
        a = a.encode("UTF-8","ignore")
        file.write(a)
        file.close()
        return 1

if __name__ == '__main__':
    schools = [#大陆高校
                #其他高校
    ]
	
    # 禁用安全请求警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    for i in range(len(schools)):
        print(i+1)
        if get_json(schools[i], 30, 0) == 0 :
            print("none")

        limit=100
        offset=30
        while True :
            if get_json(schools[i], limit, offset) == 0 :
                break
            else:
                offset = offset+100
                
    print("Done!")
