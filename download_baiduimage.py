import requests

def get_page_index(keyword,page):
    for i in range(30,30*page+30,30):
        data={
            'tn': 'resultjson_com',
            'ipn':'rj',
            'ct': '201326592',
            'is': '',
            'fp':'result',
            'queryWord':keyword,
            'cl':'2',
            'lm':'-1',
            'ie':'utf - 8',
            'oe':'utf - 8',
            'adpicid':'',
            'st':'-1',
            'z':'',
            'ic':'0',
            'word':keyword,
            's':'',
            'se':'',
            'tab':'',
            'width':'',
            'height':'',
            'face':'0',
            'istype':'2',
            'qc':'',
            'nc':'1',
            'fr':'',
            'pn':i,
            'rn':'30',
            'gsm':'1e',
            '1502988509180':''
        }
    url='https://image.baidu.com/search/index?'
