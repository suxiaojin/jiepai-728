import requests
from urllib.parse import urlencode
import json
from requests.exceptions import RequestException
from hashlib import md5
import os

def get_page_index(keyword,page):
    for i in range(30,30*int(page)+30,30):
        data={
            'tn': 'resultjson_com',
            'ipn':'rj',
            'ct': 201326592,
            'is': '',
            'fp':'result',
            'queryWord':keyword,
            'cl':2,
            'lm':-1,
            'ie':'utf - 8',
            'oe':'utf - 8',
            'adpicid':'',
            'st':-1,
            'z':'',
            'ic':0,
            'word':keyword,
            's':'',
            'se':'',
            'tab':'',
            'width':'',
            'height':'',
            'face':0,
            'istype':2,
            'qc':'',
            'nc':1,
            'fr':'',
            'pn':i,
            'rn':30,
            'gsm':'1e',
            '1502988509180':''
                             }
        url='https://image.baidu.com/search/acjson?' + urlencode(data)
        try:
            response=requests.get(url)
            if response.status_code==200:
                return response.text
            return None
        except RequestException:
            print('索引页出错')
            return None

def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('thumbURL')

def download_images(url):
    print('downloading images',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
             save_images(response.content)
        return None
    except RequestException:
        print('请求图片出错',url)
        return None

def save_images(content):
    file_path='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
#    count=1
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()
#            count+=1
#    print('total %d images' %count)


def main():
    obj=input('pls input image object:')
    page=input('pls input pages:')
    html=get_page_index(obj, page)
    if html:
        urls=parse_page_index(html)
        for url in urls:
            download_images(url)


if __name__=='__main__':
    main()

