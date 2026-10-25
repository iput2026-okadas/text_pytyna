import os

class Dictionary(object):
    def __init__(self):
        """Dictionaryオブジェクトの初期化処理"""
        #ピティナのランダム辞書作成
        self.ramdom = self.make_random_list()
        #パターン辞書作成
        self.pattern = self.make_pattern_list()

    def make_random_list(self):
        """ランダム辞書ファイルのデータを読み込んでリストrandomに格納

        Returns:
            list:ランダム辞書の応答フレーズを格納したリスト
        """
        #random
        path = os.path.join(os.path.dirname(__file__),'dics','random.txt')

        rfile = open(path,'r',encoding ='utf_8')
        #各行を要素としてリスト格納
        r_lines = rfile.readlines() #全行を読み、1行を1要素とするリストにする
        #rfile.readlines()はPython標準のやつ

        rfile.close()
        #末尾の改行と空白文字を取り除いてリストrandom_listに格納
        random_list =[]
        for line in r_lines:
            str =line.rstrip('\n')
            if(str!=''):
                random_list.append(str)
        return random_list

    def make_pattern_dictionary(self):
        """パターン辞書ファイルのデータを辞書オブジェクトpatternに格納

        Returns:
            dict:パターン辞書のパターンと応用フレーズを格納したdictオブジェクト

        ・辞書オブジェクトpatternの構造
        {
            'pattern':[パターンのリスト]
            'phrases':[パターンに対応する応答フレーズのリスト]
        }
        """
        path = os.path.join(os.path.dirname(__file__),'dics','pattern.txt')
        #Pattern辞書オープン
        pfile = open(path,'r',encoding='utf_8')
        #各行を要素としてリスト追加
        p_lines = pfile.readlines()

        pfile.close()
        #末尾の改行と空白文字を取り除いてリストpattern_listに格納
        pattern_list = []
        for line in p_lines:
            str = line.rstrip('\n')
            if(str!=''):
                pattern_list.append(str)

        #１行をタブで切り分けて辞書オブジェクトpattern_dictに格納
        #'pattern'キー：正規表現のパターン
        #'pattern'キー：応答フレーズ（メッセージ）
        pattern_dict={}
        for line in pattern_list:
            ptn,prs=line.split('\t')#多重代入
            pattern_dict.setdefault('pattern',[]).append(ptn)
            pattern_dict.setdefault('phrases',[]).append(prs)
        return pattern_dict

