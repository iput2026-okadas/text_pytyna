import random
import os


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
    def response(self, input):
        """response()をオーバーライド、おうむ返しの返答をする"""
        return '{}って何？'.format(input)


class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス"""
    def __init__(self, name):
        super().__init__(name)
        self.responses = []
        path = os.path.join(os.path.dirname(__file__), 'dics', 'random.txt')
        rfile = open(path, 'r', encoding='utf-8')
        r_lines = rfile.readlines()
        rfile.close()
        for line in r_lines:
            str = line.rstrip('\n')
            if str != '':
                self.responses.append(str)

    def response(self, input):
        return random.choice(self.responses)