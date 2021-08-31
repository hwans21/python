'''
순위 이미지 가수명 앨범명 곡명
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter
from io import BytesIO
import urllib.request as req
d = datetime.today()

file_path = f'C:/Users/hwans/Develop/Python/crawling/멜론일간차트순위_{d.year}_{d.month}_{d.day}.xlsx'

workbook = xlsxwriter.Workbook(file_path)
worksheet = workbook.add_worksheet()

chrome_option = Options()
chrome_option.add_argument('--headless')
browser = webdriver.Chrome(r'C:\Users\hwans\Develop\Python\crawling\chromedriver.exe',options=chrome_option)
target_page = 'https://www.melon.com/chart/index.htm'
browser.get(target_page)

browser.implicitly_wait(5)

worksheet.write('A1','순위')
worksheet.write('B1','이미지')
worksheet.write('C1','가수명')
worksheet.write('D1','곡명')
worksheet.write('E1','앨범명')

cnt = 2

soup = BeautifulSoup(browser.page_source,'html.parser')

list100 = soup.find_all('tr',class_='lst50') +soup.find_all('tr',class_='lst100')
for song in list100:
    print('-'*40)
    rank = song.select_one('td > div > span.rank').text
    print(f'{rank}위')
    img_url = song.select_one('td > div > a > img')['src']
    print('이미지 링크 :',img_url)
    song_name = song.select_one('td div.wrap_song_info div.rank01 span').text.strip()
    print('곡명',song_name)
    singer = song.select_one('td div.wrap_song_info div.rank02 span').text.strip()
    print('가수',singer)
    album = song.select_one('td div.wrap_song_info div.rank03 a').text.strip()
    print('앨범명',album)
    try:

        img_data = BytesIO(req.urlopen(img_url).read())
        worksheet.insert_image(f'B{cnt}',img_url,{'image_data':img_data,'x_scale':1,'y_scale':1})
    except:
        pass
    worksheet.write(f'A{cnt}',rank)
    worksheet.write(f'C{cnt}',singer)
    worksheet.write(f'D{cnt}',song_name)
    worksheet.write(f'E{cnt}',album)

    cnt+=1
browser.close()
workbook.close()