filename = 'guest.txt'

with open(filename,'w') as file_object:
    name = input('Input ur name: ')
    file_object.write(name)