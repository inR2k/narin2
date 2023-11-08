import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EC%A0%9C%EC%A3%BC%EB%8F%84+%EA%B8%B0%EB%85%90%ED%92%88'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = soup.find_all('a', {'class': 'api_txt'})
urls = soup.find_all('a', href=True)

for i in range(len(titles)):
    print('Title:', titles[i].get_text())
    print('URL:', urls[i]['href'])
    print()
