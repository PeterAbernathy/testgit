import json

num = input('tell me ur fav num: ')
filename = 'fav_num.json'
with open(filename,'w') as file_obj:
    json.dump(num,file_obj)
    