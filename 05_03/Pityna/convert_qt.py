from PyQt5 import uic
import os

#qt_PityaUI.ui のフルパスを取得
path_ui = os.path.join(os.path.dirname(__file__),'qt_Pityna.ui')

# QT Designer の出力ファイルを読み取りモードで開く
fin = open(path_ui, 'r', encoding='utf-8')
#qt_Putynaui.py のフルパスを取得
path_py = os.path.join(os.path.dirname(__file__),'qt_Pitynaui.py')
#Pthon形式ファイルを書き込みモードで開く
fout = open(path_py, 'w', encoding='utf-8')
#コンバートを開始
uic.compileUi(fin, fout) 
#2つのファイルを閉じる
fin.close()
fout.close()