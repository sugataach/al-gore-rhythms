n = 5

for idx in range(n-1):
    print((n-idx) * ' ' + (2*idx+1) * '*')

for i in range(n + 1):
    numWhite = n - i
    print ' ' * numWhite + '* ' * i
for idx in range(n-1, -1, -1):
    print((n-idx) * ' ' + (2*idx+1) * '*')
