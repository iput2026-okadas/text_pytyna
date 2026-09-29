import pityna

def prompt(obj):
    """ピュティナのプロンプト作成"""
    return obj.get_name() + '+' + obj.get_responder_name() + '>'

print('Pityna System prototype : pityna')
pityna = pityna.pityna('pityna')

#対話処理
while True:
    inputs =input('>')#文字列取得
    if not inputs:
        print('バイバイ')
        break
        #応答文字列取得
    response = pityna.dialogue(inputs)
    print(prompt(pityna),response)
