from numpy import unpackbits
import sys
a=open(sys.argv[1]).read()
b=open(sys.argv[2], 'w')
x=unpackbits(bytearray(a))

for x in x[:len(x)-1-list(x[::-1]).index(1)]:
    b.write(str(x))
    