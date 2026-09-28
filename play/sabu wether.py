import requests
from bs4 import BeautifulSoup

url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"  # 東京
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# ステータスコード確認
print(response.status_code)  # 200ならOK

# HTML全体を整形して先頭1000文字だけ表示
print(soup.prettify()[:1000])
