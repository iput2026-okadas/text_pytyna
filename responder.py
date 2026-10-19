import random
import os

class Responder(object):
    """応答クラスのスーパークラス"""
    def __init__(self,name):
        """responderオブジェクトの名前をnameに格納"""
        self.name = name
        #ランダム辞書のデータ保持
        self.responses = []
        #ramdom.txtのパスを取得
        path=os.path.join(os.path.dirname(__file__), 'dics', 'random.txt') 
        #ランダム辞書のデータを読み取りモードでオープン
        rfile=open(path, 'r', encoding='utf-8')
        #1行のテキストを要素とするリストを作成
        r_lines=rfile.readlines()
        #ファイルオブジェクトをクローズ
        rfile.close()
        #末尾の開業を取り除き、空文字出なければリスト末尾に要素として追加
        for line in r_lines:
            str = line.rstrip('\n')
            if (str!=''):
                self.responses.append(str)

    def response(self,input):
        """オーバーライドを前提としたresponse()メソッド"""
        return(random.choice(self.responses))
    
class RepeatReaponder(Responder):
    """おうむ返し用のサブクラス"""
    def response(self,input):
        """response()をオーバーライド、おうむ返しの返答をする"""
        return '{}って何？'.format(input)
    
class RandomResponder(Responder):
    """ランダム応答のサブクラス"""
    def __init__(self, name):
        super().__init__(name)
        self.responses =['いい天気やね','何となくそう思う','10円拾った']

    def response(self, input):
        return (random.choice(self.responses))
    