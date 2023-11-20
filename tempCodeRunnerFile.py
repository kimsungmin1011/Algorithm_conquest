import requests
from bs4 import BeautifulSoup

# 웹 페이지 가져오기
url = "https://www.naver.com"
response = requests.get(url)

# 응답의 HTML을 파싱하기
soup = BeautifulSoup(response.text, "html.parser")

# 원하는 요소 찾기
elements = soup.find_all("태그명", class_="클래스명")

# 원하는 데이터 추출하기
for element in elements:
    print(element.text)
