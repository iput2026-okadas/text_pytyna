import responder

class pityna(object):
    """ピティナ本体"""
    def __init__(self,name):
        self.name = name
        self.responder = responder.RandomResponder('Random')
    
    def dialogue(self, input):
        """応答オブジェクトのresponse（）を呼び出し応答文字列の取得"""
        return self.responder.response(input)
    
    def get_responder_name(self):
        """応答に使用されたオブジェクト名を返す"""
        return self.responder.name
    
    def get_name(self):
        """pitynaオブジェクトの名前を返す"""
        return self.name