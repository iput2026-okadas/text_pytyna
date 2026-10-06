from PyQt5 import QtWidgets
import qt_pitynaui
#import pityna

class MainWindow(QtWidgets.QMainWindow):
    """
    QtWidgers.QMainWindowを継承したサブクラス 
    UI画面構築行う
    
    Attribute:
        pityna(obj):Pitynaクラスのオブジェクト
        action(bool):ラジオボタンの状態保持
        ui(obj):Ui_MainWindowオブジェクト保持   
    """
    def hidden_responder_name(self):
        """RadioButton_2がオンの時に呼ばれるイベントハンドラー"""
        self.action = False

    def __init__(self):
        super().__init__()
        #self.pityna = pityna.Pityna('pityna')
        self.action = True
        self.ui = qt_pitynaui.Ui_MainWindow()
        self.ui.setupUi(self)

    def prompt(self):
        """
        ピティナのプロンプト
        """
        p=self.pityna.det_name()
        if self.action == True:
            p +=':' + self.pityna.get_responder_name()
        return p + '>'

    def button_talk_slot(self):
        """
        トークボタンのイベントハンドラー
        """
        value = self.ui.lineEdit.text()

        if not value:
            #未入力の場合の表示
            self.ui.LabelReaponce.setText('何か入力してください')
        else:
            #発言があれば対話オブジェクトを実行
            #応答メッセージを出力
            response = self.pityna.dialogue(value)
            #プロンプト記号にユーザーの発言を連結してログ用のリストに出力
            self.ui.LabelReaponce.setText(response)
            #ピティナのプロンプト記号に応答メッセージを連結してログ用のリストに出力
            self.putlog('>'+value)
            self.putlog(self.prompt() + response)
            self.ui.lineEdit.clear()

    def closeEvent(self, event):
        """
        ウィンドウを閉じるcloseメソッド実行時にQCloseEventによって呼ばれる

        Overrides:
            ・メッセージボックスを表示
            ・[yes]が押された場合はイベント続行してウィジェットを閉じる
            ・[no]が押された場合はイベントを中止してウィジェットを閉じない

        Args:
            event(obj):閉じるイベント発生時に渡されるQCloseEventオブジェクト
        """
        reply = QtWidgets.QMessageBox.question(self, '確認', '終了してもよろしいですか？',
                                               buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        #yesが押された場合はイベントを続行してウィジェットを閉じるnoクリックで閉じる処理を無効か
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def show_responder_name(self):
        """
        RadioButton_1がオンと時に呼ばれるイベントハンドラー
        """
        #ラジオボタンの状態を保持する変数(action)をTrueに設定
        self.action = True

    def hide_responder_name(self):
        """
        RadioButton_2がオンと時に呼ばれるイベントハンドラー
        """
        #ラジオボタンの状態を保持する変数(action)をFalseに設定
        self.action = False

            
        
       
