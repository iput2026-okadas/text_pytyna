"""
Mosquittoの復習：MQTT接続失敗の場合、原因を自動検出ツール

やることリスト
    1.外部コマンドエラー確認（ping）
    2.DNSのエラー確認終了
    3.TCP接続確認
"""
import socket  #ネットワーク関連（DNS解決）
import subprocess#pingを実行して結果の取得するモジュール
import paho.mqtt.client as mqtt#mqttクライアントライブラリをあだ名化
BROKER = "test.mosquitto.org"#ホスト名
PORT = 1883  #接続ポート
TOPIC = "tk240278/test"#トピック名
def check_network():#ネットワーク接続チェック関数作成
    print("[1] ネットワーク接続確認中...")
    try:
        result = subprocess.run(["ping", "-c", "1", "8.8.8.8"],#pingを使ってGoogeのDNSサーバー（８.８.８.８）に送信
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)#出力をキャプチャ（記録）してresultに格納。：：-cはunix系で一回送る
        if result.returncode == 0:  #pingの戻り値確認
            print(":チェックマーク_緑: ネットワーク接続OK")
            return True
        else:
            print(":x: ネットワークに接続されていません")
            return False
    except Exception as e:
        print(":警告: ネットワーク確認エラー:", e)
        return False
#ここで1.ping(外部コマンド)のエラー確認終了

def check_dns():#DNS解決を確認関数作成
    print("\n[2] DNS解決確認中...")#確認開始
    try:
        ip = socket.gethostbyname(BROKER)#ホスト名をDNSで確認。IPにipが入ればおk
        print(f":チェックマーク_緑: DNS解決OK: {BROKER} → {ip}")
        return True
    except socket.gaierror:
        print(":x: DNS解決エラー: ホスト名が間違っている可能性")
        return False
#ここで2.DNSのエラー確認終了
def check_port():#指定ポートへのTCP接続確認関数作成
    print("\n[3] ポート接続確認中...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#IPv4（アドレス形式）・TCP（通信）のソケット（入口、受話器的なもの）を作成
        sock.settimeout(3)#ソケットのタイムアウト作成
        result = sock.connect_ex((BROKER, PORT))#ブローカに接続 connect_EXは例外を投げない=0は成功
        sock.close()
        if result == 0:
            print(f":チェックマーク_緑: ポート{PORT}に接続OK")
            return True
        else:
            print(f":x: ポート{PORT}に接続失敗（ブローカ停止やファイアウォールの可能性）")
            return False
    except Exception as e:
        print(":警告: ポート確認エラー:", e)
        return False
#ここで3.TCP接続確認終了
def check_mqtt():#mqttとメッセージ送信確認関数作成
    print("\n[4] MQTT接続確認中...")
    client = mqtt.Client()#pah0-mqttのクライアントインスタンス作成（接続、publishに使用）
    try:
        client.connect(BROKER, PORT, 5)#ブローカー接続_５秒間間を開ける
        client.publish(TOPIC, "diagnostic test message")#トピックにメッセージ送信
        client.disconnect()#切断
        print(":チェックマーク_緑: MQTT接続・送信OK")
        return True
    except Exception as e:
        print(f":x: MQTT接続エラー: {e}")
        return False
#4.mqtt_メッセージ確認終了
def main():#スクリプトのメイン処理！
    print("=== MQTT接続診断ツール ===\n")
    steps = [
        ("ネットワーク", check_network),
        ("DNS", check_dns),
        ("ポート", check_port),
        ("MQTT", check_mqtt)
    ]
    all_ok = True
    for name, func in steps:#stepsの格タプルを表示名と関数に展開ループ
        ok = func()
        if not ok:
            all_ok = False
    print("\n=== 診断結果 ===")
    if all_ok:
        print(":チェックマーク_緑: すべての接続テスト成功！通信は正常です。")
    else:
        print(":警告: どこかの段階で問題が発生しています。上記ログを確認してください。")
if __name__ == "__main__":
    main()







