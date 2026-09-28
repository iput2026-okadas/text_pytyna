#2
test_list=[]
test_list.append(1)
print(test_list)
"""
まとめて追加する場合はextend
"""
test_list.extend((2,3))# extend[_] ではなく extend(_)
print(test_list)

#3
dictionary_list={}
dictionary_list={'a':'A','b':'B','c':'C'}
print(dictionary_list)
'''
辞書（dict）は {キー: 値,} で作る。

文字列キーや文字列値は "_" または '_' で囲む必要がある。

空の辞書は {} で作れる。
'''
