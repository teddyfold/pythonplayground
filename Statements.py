a = 3
b = 2

# swapping a nd b if a > b
if a > b:
    temp = b;
    b = a;
    a = temp

name = 'Test'
if name == 'Zhi':
    print "found {name}".format(name=name)
elif name == 'xin':
    print "found different person"
else:
    print "not found"
