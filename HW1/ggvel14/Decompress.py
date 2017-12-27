# -*- coding: utf-8 -*-
import helper,sys
from numpy import unpackbits, packbits

code=open(sys.argv[1]).read().split()
a=open(sys.argv[2], 'rb').read()
out=open(sys.argv[3], 'w')

b=''
a=unpackbits(bytearray(a))
for x in a[:len(a)-1-list(a[::-1]).index(1)]:
    b+=str(x)

dic=helper.buildAlpDictionary(code)

cc=''
text=''
for x in b:
    if cc+x in dic:
        text+=dic[cc+x]
        cc=''
    else:
        cc+=x

out.write(text)