import os
path=os.path.join(os.path.dirname(__file__), 'dics', 'random.txt') 

file = open(path, 'r', encoding='utf-8')
data = file.read()
file.close()
print(data)