
"""
self =「今この処理をしている自分自身のオブジェクト」ここではpitynaのこと
"""
class Pityna:
    #ピティナ本体

    def __init__ (self, name):
        """変数の初期化"""
        self.name = name
        self.responder = Responder('Repeat')#Responderオブジェクトを生成しインスタンス変数に代入

    def dialogue(self, input):
        """応答オブジェクトのresponese()を呼び出して応答文字を取得"""
        return self.responder.response(input)
    
    def get_responder_name(self):
        """応答に使用されたオブジェクト名を返す"""
        return self.responder.name
    
    def get_name(self):
        """pitynaオブジェクト名を返す"""
        return self.name
    
class Responder:
    #応答クラス

    def __init__(self, name):
        """responeオブジェクトの名前をnameに格納"""
        self.name=name

    def response(self, input):
        """応答文字を作成し返す"""
        return '{}って何？'.format(input)
    
###############
#実行ブロック
###############
def prompt(obj):
    """ピュティナのプロンプト作成"""
    return obj.get_name() + '+' + obj.get_responder_name() + '>'

#ここから開始
print('Pityna System prototype : pityna')

pityna = Pityna('Pityna')#Pytinaオブジェクト生成

#対話処理
while True:
    inputs =input('>')#文字列取得
    if not inputs:
        print('バイバイ')
        break
    else:
        #応答文字列取得
        response =  pityna.dialogue(inputs)
        print(prompt(pityna),response)