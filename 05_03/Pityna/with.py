import os

path=os.path.join(os.path.dirname(__file__), 'dics', 'random.txt') 
with open(path, 'r', encoding='utf-8') as file:
    list = [elm.rstrip() for elm in file.readlines()]
    print(list)