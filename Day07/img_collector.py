print('# 최초 실행 시 약간의 로딩이 발생할 수 있으니 잠시만 기다려 주세요!(최대 1분)')
print('인터넷 연결이 되어 있어야 합니다.!! 제작자 : 2subtanker')

# 운영체제에서 제공되는 여러기능(폴더 생성)
import os
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
import time as t
from selenium import webdriver


opener = req.build_opener()
opener.addheaders = [('User-agent',UserAgent().ie)]
req.install_opener(opener)

# 네이버 이미지 기본 URL
base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

print('### 검색어를 입력하시면 해당 검색어에 맞는 이미지를 50개 다운로드 받습니다.')
print('### 이미지 자료는 네이버 검색 자료를 수집합니다.')
print('### 다운받은 이미지는 C드라이브 imagedown폴더에 자동 저장됩니다.')

# 검색어
s = input('### 검색어 입력:')
quote = rep.quote_plus(s)

url = base + quote
print(url)

# 저장 경로
save_path = 'c:/imagedown/'

# 폴더 생성(예외 처리)
try:
    # 기존 폴더 있는지 체크
    if not os.path.isdir(save_path):
        #없으면 폴더 생성
        os.mkdir(save_path)
except OSError as e:
        print('폴더 생성 실패!')
        print('폴더 이름:', e.filename)
browser = webdriver.Chrome(r'C:\Users\hwans\Develop\Python\crawling\chromedriver.exe')
browser.get(url)

browser.implicitly_wait(5)

res = browser.page_source


# res = req.urlopen(url).read()

# bs4 초기화
soup = BeautifulSoup(res, 'html.parser')
print(soup)

img_list = soup.find_all('div',class_='thumb')
print(img_list)