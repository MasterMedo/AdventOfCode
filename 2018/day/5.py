purge = lambda s: reduce(lambda x, y: x[:-1] if x and ord(x[-1])^32 == ord(y) else x+y, s)
data = purge(open('../input/5.txt').read().strip())

print len(data)
print min(len(purge(filter(lambda x: x.upper() != c, data))) for c in map(chr, range(65, 91)))
