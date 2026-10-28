import random
import re


class Responder(object):
    """応答クラスのスーパークラス"""
    def __init__(self, name):
        """responderオブジェクトの名前をnameに格納"""
        self.name = name

    def response(self, input):
        """オーバーライドを前提としたresponse()メソッド"""
        return ''


class RepeatResponder(Responder):
    """おうむ返し用のサブクラス"""
    def __init__(self, name):
        super().__init__(name)

    def response(self, name):
        """response()をオーバーライド、おうむ返しの返答をする"""
        return '{}って何？'.format(input)


class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス

    """

    def __init__(self, name,dic_random):
        super().__init__(name)
        self.random = dic_random

    def response(self, input):
        return random.choice(self.responses)

class PatternResponder(Responder):
    """パターンに反応するためのサブクラス"""
    def __init__(self,name,dictionary):
        super().__init__(name)
        self.dictionary = dictionary

    def response(self,input):
        """パターンにマッチした場合に応答フレーズを抽出して返す"""
        for ptn,prs in zip(
            self.doctinary.pattern['pattern'],
            self.dictinary.pattern['phrases']
        ):
            m =re.serch(ptn,input)
            if m:
                resp =random.choice(prs.split('|'))
                return re.sub('%match%',m.group(),resp)
        return random.choice(self.dictionary.random)