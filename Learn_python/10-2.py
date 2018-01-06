filename = 'text_files/learning_python.txt'
with open(filename) as f:
    for line in f:

        print(line.replace('Python','C'))