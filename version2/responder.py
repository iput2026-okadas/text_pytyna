import random

class Responder(object):
    """応答クラスのスーパークラス"""
    def __init__(self,name):
        """responderオブジェクトの名前をnameに格納"""
        self.name = name

    def response(self,input):
        """オーバーライドを前提としたresponse()メソッド"""
        return''
    
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
    