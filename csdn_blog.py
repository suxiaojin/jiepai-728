from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq

browser=webdriver.Chrome()
browser.get('http://so.csdn.net/so/')
wait=WebDriverWait(browser,10)

def search():
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#queryform > div.search-text-con > input')))
        button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#queryform > div.search-btn-con > input')))
        input.send_keys('python')
        button.click()
        get_products()
    except TimeoutException:
        search()

def next_page(page_numb):
    try:
        input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#p1')))
        button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-go > button')))
        input.clear()
        input.send_keys(page_numb)
        button.click()
        get_products()
    except TimeoutException:
        next_page(page_numb)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.search-list-con .search-list')))
    html=browser.page_source
    doc=pq(html)
    items=doc('.search-list-con .search-list').items()
    for item in items:
        product={
            'title':item.find('.search-list J_search').text(),
            'content':item.find('.search-detail').text(),
            'url':item.find('.search-link').text()
        }
        print(product)

def main():
    search()
    for i in range(1,11):
        next_page(i)

if __name__=='__main__':
    main()