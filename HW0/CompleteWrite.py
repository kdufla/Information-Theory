from numpy import packbits
import sys
a=open(sys.argv[1]).read()
b=open(sys.argv[2], 'wb')
a=a+'1'+ ('' if len(a)%8==7 else '0'*(8-((len(a)+1)%8)))

def translate(a):
    for x in a:
        if x=='0':
            yield 0
        else:
            yield 1

b.write(packbits(list(translate(a))))
