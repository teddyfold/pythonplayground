#define a dict (map)
myDict = {'offset': 1.5, 'coefficient': 2.5};

#look through all keys
for key in myDict.keys():
    print 'Operating on {keyValue}'.format(keyValue=key)
    myDict[key] = myDict[key] ** 2

print 'End of Operation'

print myDict

t = (1, 2, 3, [4, 5])
t1 = (4, 5, 6)
print t[3][0]
print t.count([4, 5])
