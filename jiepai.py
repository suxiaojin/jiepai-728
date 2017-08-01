import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
import os
from hashlib import md5

def get_index_page(st,q):
    data={
        'rn': '72',
        'st': st,
        'q': q,
        't': '1501555986724'
    }
    url = 'http://image.chinaso.com/getpic?' + urlencode(data)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def parser_index_page(html):
    data=json.loads(html)
    if data and 'arrResults' in data.keys():
        for item in data.get('arrResults'):
            yield item.get('url')

def download_images(url):
    print('正在下载',url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            save_images(response.content)
        return None
    except RequestException:
        print('请求图片出错')
        return None

def save_images(content):
    file_path= '{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()

def main(st):
    html=get_index_page(st,'mug')
#    print(html)
    if html:
        urls=parser_index_page(html)
        for url in urls:
            download_images(url)

if __name__=='__main__':
    main(i*72 for i in range(6))