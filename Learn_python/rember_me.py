import json

username = input('whats ur name? ')
filename = 'username.jason'

with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print('')