from numpy import unpackbits
import sys
a=open(sys.argv[1]).read()
b=open(sys.argv[2], 'wb')
for x in unpackbits(bytearray(a)):
    b.write(str(x))
