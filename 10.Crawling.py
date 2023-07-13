"""
import urllib.request

#데이터 읽기
response = urllib.request.urlopen("https://www.kakao.com/")
data = response.read()

#읽어온 데이터의 인코딩 설정
encoding = response.info().get_content_charset()
html = data.decode(encoding)

#화면 출력
print(html)
"""


"""
#URL에 한글이 포함된 경우
import urllib.request
response = urllib.request.urlopen("https://search.hani.co.kr/search?command=query&media=common&searchword=사이버가수아담&x=0&y=0&_ga=2.225940573.611667888.1689238630-1387075702.1689238630")
data = response.read()

#읽어온 데이터의 인코딩 설정
encoding = response.info().get_content_charset()
html = data.decode(encoding)

#화면 출력
print(html)
"""


"""
#URL에 한글이 포함된 경우
import urllib.request
from urllib.parse import quote

keyword = quote("사이버가수아담")
response = urllib.request.urlopen("https://search.hani.co.kr/search?command=query&media=common&searchword=" + keyword + "&x=0&y=0&_ga=2.225940573.611667888.1689238630-1387075702.1689238630")
data = response.read()

#읽어온 데이터의 인코딩 설정
encoding = response.info().get_content_charset()
html = data.decode(encoding)

#화면 출력
print(html)
"""


"""
import requests

# GET
resp = requests.get('http://httpbin.org/get')
print(resp.text)

# POST
dic = {"id": "ggangpae1", "name": "박문석", "age": 40}
resp = requests.post('http://httpbin.org/post', data=dic)
print(resp.text)

resp = requests.put('http://httpbin.org/put')
print(resp.text)

resp = requests.delete('http://httpbin.org/delete')
print(resp.text)
"""

"""
import requests
res = requests.get('https://www.python.org/')
# resp.raise_for_status()

if (res.status_code == requests.codes.ok):
    html = res.text
    print(html)
"""


"""
import requests
try:
    res = requests.get('https://www.naver.com') # 네이버 홈
    print(res.encoding)
    res = requests.get('http://www.tjoeun.co.kr/') # 더조은 홈페이지
    print(res.encoding)
except Exception as e:
    print("예외발생:", e)
"""


"""
import requests

imgurl = 'http://www.onlifezone.com/files/attach/images/962811/376/321/005/2.jpg'
imgname = 'data/' + imgurl.split('/')[-1]
try:
    res = requests.get(imgurl)
    with open(imgname, 'wb') as h:
        img = res.content
        h.write(img)
except Exception as e:
    print(e)
"""


"""
import requests
import json
url = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=PM9&rect=126.95,37.55,127.0,37.60'
headers = {'Authorization': 'KakaoAK {}'.format('c454c0e64688ce2bde2dfff9cceced87')}
data = requests.post(url, headers=headers)
result = json.loads(data.text) #파싱한 결과
#print(result)
documents = result['documents']
for data in documents:
    print(format(data['place_name'], '30s'), end='\t')
    print(format(data['address_name'], '30s'))
"""

"""
import requests, bs4

try:
    resp = requests.get('http://finance.daum.net/')
    resp.raise_for_status()

    html = resp.text
    bs = bs4.BeautifulSoup(html, 'html.parser')

except Exception as e:
    print("예외 발생:", e)

else:
    print(bs.body.span.get_text())
"""


"""
import requests, bs4
from urllib.parse import quote
import re

try:
    # wikipedia 에서 기계_학습 검색 결과 가져오기
    keyword = '기계_학습'
    keyword = quote(keyword)
    resp = requests.get('https://ko.wikipedia.org/wiki/' + keyword)
    resp.raise_for_status()

    html = resp.text
    # 텍스트를 DOM으로 만들기
    bs = bs4.BeautifulSoup(html, 'html.parser')
except Exception as e:
    print("예외 발생1:", e)
else:
    #a 태그 전부 가져오기
    for link in bs.findAll('a'):
        #속성에 href 가 있는 경우
        if 'href' in link.attrs:
            #href 안의 내용 중 /wiki/가 포함된 것만 골라내기
            href = link.attrs['href']
            p = re.compile('^(/wiki/)')
            if p.search(href) != None:
                print(href)
"""


"""
#네이버 주식에서 타이틀 가져오기
import requests, bs4

try:
    resp = requests.get('https://finance.naver.com/')
    resp.raise_for_status()

    resp.encoding = 'euc-kr'
    html = resp.text
    bs = bs4.BeautifulSoup(html, 'html.parser')
    tags = bs.select('span > a')  # Top 뉴스
    title = tags[0].getText()
    print(title)
except Exception as e:
    print("예외 발생:", e)
"""


"""
#네이버 팟 캐스트에서 타이틀 가져오기
import requests, bs4
try:
    res = requests.get('https://tv.naver.com/r/category/drama')
    res.raise_for_status()

    html = res.text
    bs = bs4.BeautifulSoup(html, 'html.parser')
    tags = bs.select('strong span')
    for title in tags:
        print(title.getText())
except Exception as e:
    print("예외 발생:", e)
"""


"""
#온도, 습도 출력
import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.select('#weather_table > tbody')

loc = []
temp =[]
hum=[]


# 데이터를 저장할 리스트 생성
for tr in table[0].find_all('tr'):      # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))    # 모든 <td> 태그를 찾아서 리스트로 만듦
    for td in tds:                   # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        if td.find('a'):             # <td> 안에 <a> 태그가 있으면(지점인지 확인)
            loc.append(td.find('a').text)    # <a> 태그 안에서 지점을 가져옴
            temp.append(tds[5].text)    # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
            hum.append(tds[9].text)       # <td> 태그 리스트의 열 번째(인덱스 9)에서 습도를 가져옴
print('도시 이름:', loc[0:5])
print('현재 온도:', temp[0:5])
print('습도:', hum[0:5])
print()
print()

cities = ['서울', '인천', '대전', '대구', '광주', '부산', '울산', '창원']
temperatures = []
humidities = []
for city in cities:
    j = 0
    for c in loc:
        if city == c:
            temperatures.append(temp[j])
            humidities.append(hum[j])
            break
        j = j + 1

print('도시 이름:', cities)
print('현재 온도:', temperatures)
print('습도:', humidities)
"""


"""
import requests
import bs4
from html.parser import HTMLParser
from io import StringIO


# 문자열에서 태그를 제거하기 위한 클래스 와 함수
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


url = 'http://www.hani.co.kr/rss/'
response = requests.get(url)
print(response.text)

#파싱 객체 생성
rss = bs4.BeautifulSoup(response.text, "html.parser")
items = rss.find_all('item')

for item in items:
    print(strip_tags(item.find('title').getText()), end=':')
    print(item.find('link').getText())
"""

import requests
import bs4
url = 'https://dapi.kakao.com/v2/local/search/category.xml?category_group_code=PM9&rect=127.0561466,37.5058277,127.0602340,37.5142554'
headers = {'Authorization': 'KakaoAK {}'.format('c454c0e64688ce2bde2dfff9cceced87')}
response = requests.post(url, headers=headers)
#print(response.text)

#파싱 객체 생성
xml = bs4.BeautifulSoup(response.text, "html.parser")
place_names = xml.find_all('place_name')
address_names = xml.find_all('address_name')

i = 0
for place_name in place_names:
    address_name = address_names[i]
    print(format(place_name.getText(), '30s'), end='\t')
    print(format(address_name.getText(), '30s'), end='\t')
    i = i + 1
