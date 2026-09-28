"""
raspberry piでDHT22の温度湿度センサーを使ってAmbient(iotクラウドサービス）にデータを送るプログラムをMacのVSCのみで擬似練習する

ambient URL=https://ambidata.io/bd/board.html?id=101388
"""
import time
import random
import ambient

my_channel_id=95787
my_write_key="39d4ec366b4dfeb7"
ambi = ambient.Ambient(my_channel_id, my_write_key)#ambientAPIと接続するオブジェクト

count=20#カウンター
while count>0:
    try:
        #疑似センサ
        temperature_c=round(random.uniform(20.0,30.0),1)#20~30でランダムな少数を出す
        humidity=round(random.uniform(40.0,60.0),1)#round(a,1)は少数第一まで

        print(f"{count}回目:{temperature_c}°C,{humidity}%")#"{}"はフｫーマット文字列で変数を埋め込む特殊記号
        r=ambi.send({"d1":temperature_c,"d2":humidity})#ambientのグラフの名がd1,d2なので言わば形式
        count-=1 #カウントするごとに減る
        time.sleep(10)#10秒間停止させるアクセス過多になるから

    except Exception as error:
        print("エラー：",error)
        break
        