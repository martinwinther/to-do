filenames = ['007 a.txt', '007 b.txt', '007 c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)