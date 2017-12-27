# -*- coding: utf-8 -*-
import sys
a=open(sys.argv[1]).read()
b=open(sys.argv[2], 'w')

alp=' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
singles={}
couples={}
for x in alp:
    singles[x]=0
    for y in alp:
        couples[x+y]=0

for x in range(len(a)-1):
    singles[a[x]]+=1
    couples[a[x:x+2]]+=1
singles[a[len(a)-1]]+=1

ln0=''
ln1=''
for x in alp:
    ln0+=str(format(singles[x]/len(a),'.7f'))+' '
    for y in alp:
        ln1+=str(format(couples[x+y]/(len(a)-1),'.7f'))+' '

b.write(ln0[:-1])
b.write('\n')
b.write(ln1[:-1])
