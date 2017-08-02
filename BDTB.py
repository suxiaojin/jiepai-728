from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
from pyquery import PyQuery as pq
import json

browser=webdriver.Chrome()
browser.get('http://www.51job.com/')
wait=WebDriverWait(browser,10)

def search():
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#kwdselectid')))
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.content > div > div.fltr.radius_5 > div > button')))
        input.send_keys('python')
        submit.click()
        total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.dw_wp > div.dw_page > div > div > div > span:nth-child(2)')))
        for item in get_products():
            save_to_file(item)
        return total.text
    except TimeoutException:
        search()

def next_page(page_numb):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#jump_page')))
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.dw_wp > div.dw_page > div > div > div > span.og_but')))
        input.clear()
        input.send_keys(page_numb)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'body > div.dw_wp > div.dw_page > div > div > div > ul > li.on'),str(page_numb)))
        for item in get_products():
            save_to_file(item)
    except TimeoutException:
        next_page(page_numb)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#resultList .el')))
    html=browser.page_source
    doc=pq(html)
    items=doc('#resultList .el').items()
    for item in items:
        yield {
            'position':item.find('.t1').text(),
            'company':item.find('.t2').text(),
            'location':item.find('.t3').text(),
            'pay':item.find('.t4').text(),
            'update':item.find('.t5').text()
        }

def save_to_file(item):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(item,ensure_ascii=False)+'\n')
        f.close()

def main():
    total=search()
    total=int(re.compile('(\d+)').search(total).group(1))
    for i in range(1,total + 1):
         next_page(i)

if __name__=='__main__':
    main()