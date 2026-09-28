#memo
'''
\nは文字列の中に入れる
＼を行の途中に入れるとコードを分割して使える、要は長いコードを改行しても一つのコードとして扱う
'''

version = 3.6
moji ="nekonikoban"

print("累乗:5**2=",5**2)

print("等しくない（not_equal）：A != a:" ,"A" != "a")

print("文字の長さ_(リストも可能)_len([1, 2, '3.6']=:", len([1, 2, '3.6']))

print("str:引数を文字列に:str(version)", 
      str(version), 
       
      "range():指定した数字を自動入力\n", 
      list(range(1, 10)),
      "特定の文字列で区切る:moji.split('n'):\n",
        moji.split("n"),

       "自動大文字化：upper\n",
       moji,"→",moji.upper(),
      )
