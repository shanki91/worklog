#!\usr\bin\python

name=''

while name != 'quit':
    name = raw_input('Wie heisst du?')
    if name == 'Tobias':
        print "Nicenstein!"
    else:
        print name, 'ist ein Huso-Name.'
