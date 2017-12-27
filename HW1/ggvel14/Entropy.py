# -*- coding: utf-8 -*-
import sys,math
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
    singles[a[x]]+=1/len(a)
    couples[a[x:x+2]]+=1/(len(a)-1)
singles[a[len(a)-1]]+=1/len(a)

entSin=format(-sum([singles[x]*math.log2(singles[x]) if singles[x]>0 else 0 for x in singles]), '.7f')
entCou=format(-sum([couples[x]*math.log2(couples[x]) if couples[x]>0 else 0 for x in couples]), '.7f')

b.write(entSin+'\n'+entCou+'\n'+format(float(entCou)-float(entSin), '.7f'))
