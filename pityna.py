import responder
"""module名ミス"""
class Pityna(object):
    """
    ピティナのクラス
    """
    def __init__(self, name):
        self.name = name
        self.responder = responder.RandomResponder('Random')

    def dialogue(self, input):
        """
        入力テキストに対してレスポンダーの応答を返す
        """
        return self.responder.response(input)

    def get_responder_name(self):
        """
        レスポンダーの名前を返す
        """
        return self.responder.name

    def get_name(self):
        """
        ピティナの名前を返す
        """
        return self.name