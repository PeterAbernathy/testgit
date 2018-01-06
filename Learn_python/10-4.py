filename = 'guest.txt'

while True:

    name = input('Input ur name: ')
    if name == '0':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name +'\n')
