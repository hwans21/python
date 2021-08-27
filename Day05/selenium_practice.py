'''
네이버로 접속하셔서 뉴스스탠드 쪽에 잇는 파란색 '네이버 뉴스'를
클릭하세요 

상단에 있는 메뉴 중 정치, 경제, 사회, 생활/문화, 세계, IT/과학
탭을 돌아다니면서 헤드라인 뉴스 4개씩 클릭해 주시면 됩니다.

뒤로가기는 driver.back() 메서드로 뒤로가기 가능합니다.

xpath를 따다보면 규칙을 발견하실 수 있을 겁니다.
반복문을 이용해서 클릭 명령을 내려 주시면 됩니다.
24개의 명령을 일일히 쓰라는게 아니에요 규칙을 꼭 발견하세요
'''

import time
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\hwans\Develop\Python\crawling\chromedriver.exe')

driver.get('https://www.naver.com')

driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)
for i in range(3,9):
    driver.find_element_by_xpath(f'//*[@id="lnb"]/ul/li[{i}]/a').click()
    time.sleep(1)
    for j in range(1,5):
        try:
            driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j}]/div[2]/ul/li[1]/div[2]/a').click()
        except:
            try:
                driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j}]/div[1]/ul/li[1]/div[2]/a').click()
            except:
                driver.find_element_by_xpath(f'//*[@id="main_content"]/div/div[2]/div[1]/div[{j}]/div[2]/ul/li[1]/div/a').click()
        time.sleep(1)
        driver.back()
        time.sleep(1)