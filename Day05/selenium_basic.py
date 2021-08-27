# 셀레늄 : 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# cmd -> pip install selenium (셀레늄 라이브러리 다운로드)
# 셀레늄 임포트
from selenium import webdriver
import time 

# 다운로드 받은 크롬 물리드라이브 가동 명령
# 크롬이 바로 종료됨(해결 -> 실행할 때 ctrl+F5 (x) ctrl+alt+n (o) )
driver = webdriver.Chrome(r'C:\Users\hwans\Develop\Python\crawling\chromedriver.exe')

# 해결안됨
# chrome_option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(r'C:\Users\hwans\Develop\Python\crawling\chromedriver.exe',chrome_options=chrome_option)



# 물리 드라이버로 사이트 이동명령
driver.get('https://www.naver.com')

'''
#자동으로 버튼이나 링크 클릭 제어하기.
login_btn = driver.find_element_by_xpath('//*[@id="account"]/a')
login_btn.click()
time.sleep(1.5)

# 자동으로 텍스트 입력하기
id_input = driver.find_element_by_xpath('//*[@id="id"]')
id_input.send_keys('hwanseo')
time.sleep(0.3)
pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('test123')
driver.find_element_by_xpath('//*[@id="log.login"]').click()

'''
# 네이버에 접속하셔서 검색창에 '오늘 날씨'를 입력하셔서
# 검색 후 가장 첫번째로 뜨는 네이버 뉴스를 띄워주세요
driver.find_element_by_xpath('//*[@id="query"]').send_keys('오늘 날씨')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="sp_nws_all1"]/div[1]/div/a').click()
