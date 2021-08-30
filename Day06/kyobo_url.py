from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

d = datetime.today()
driver = webdriver.Chrome(r'C:\Users\hwans\Develop\Python\crawling\chromedriver.exe')

file_path = f'C:/Users/hwans/Develop/Python/crawling/교보문고 베스트셀러 {d.year}_{d.month}_{d.day}.html'


driver.get('http://www.kyobobook.co.kr/index.laf')
driver.find_element_by_xpath('//*[@id="header"]/div[3]/ul[2]/li[1]/a').click();

src = driver.page_source
soup = BeautifulSoup(src,'html.parser')
div_list = soup.find_all('div',class_='detail')

 
with open(file_path,'w') as f:
    f.write('<html>')
    f.write('<head>')
    f.write('<title>')
    f.write('교보문고 베스트셀러 1~20위')
    f.write('</title>')
    f.write('</head>')
    f.write('<body>')
    f.write('교보문고 베스트셀러 1~20위<br><br>')
    rank = 0
    for div in div_list:
        rank+=1
        f.write('<strong>')
        f.write(f'순위: {rank} <br>')
        book = div.find('div', class_='title')
        book_link = book.find('a')
        f.write(f'{book_link}')
        f.write('</strong><br><hr>')
    f.write('</body>')
    f.write('</html>')