filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:5])
print(len(pi_string))