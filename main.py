import sys
from PyQt5 import QtWidgets
import mainwindow

if __name__ == "__main__":
    #QApplicationはウィンドウシステムを初期化しコマンドライン引数を使用してアプリケーションオブジェクトを構築
    app = QtWidgets.QApplication(sys.argv)

    #画面を構築するMainWindowクラスのオブジェクト生成
    win=mainwindow.MainWindow()
    #メインウィンドウを表示
    win.show()
    #メッセージループをプログラム終了まで実行　終了時は0
    ret = app.exec_()
    #終了コードを返す
    sys.exit(ret)