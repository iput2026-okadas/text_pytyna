"""
responce=recuests.get(url)
  requests：Wedページのデータ取得
  response:Wed全体のHTMLデータ

soup=BeautifulSoup(response.text,"html.parser")
  responce.text:Wedの中身
  BeutihulSoup():HTML分析からツリー構造化

a.newFeed_item_tittle
  a:HTMLのaタグ
  newFeed__item_tittle:クラス名

t.text:HTMLの文字部分を取り出す
"""


import requests
from bs4 import BeautifulSoup

url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html" 
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

#都市名
city=soup.select_one("h1").text.strip()

#天気
weather = soup.select_one("div.forecastCity > p.pict").text.strip()
temp_info = soup.select_one("div.forecastCity > p.info").text.strip()

print("🏙️", city)
print("🌤️ 天気:", weather)
print("🌡️ 気温情報:", temp_info)