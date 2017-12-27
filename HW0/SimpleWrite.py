from numpy import packbits
import sys
a=open(sys.argv[1]).read()
b=open(sys.argv[2], 'wb')

def translate(a):
    for x in a:
        if x=='0':
            yield 0
        else:
            yield 1

b.write(packbits(list(translate(a))))
