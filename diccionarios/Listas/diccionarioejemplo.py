d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': ['nj','hn'], 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    print(item)
    d3.update(item)

print(d3)

print(10*(5+3))
print(3*3+2/5+5%4)
print(10*5+3)
print(-2**4)