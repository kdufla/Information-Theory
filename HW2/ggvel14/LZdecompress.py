import sys,helper,time

a=helper.completeRead(open(sys.argv[1],'rb').read())

def getLenFromGama(gamaStr):
    idx=0
    while(gamaStr[idx]=='0'):
        idx+=1
    return int(str(gamaStr[idx:2*idx+1]),2)

def getGamaCodeLen(gamaStr):
    idx=0
    while(gamaStr[idx]=='0'):
        idx+=1
    return idx*2+1

gama=getLenFromGama(a)
l=getGamaCodeLen(a)

d=['0','1']
idx=l
size=2
fin=[]
while(idx+1<=len(a)):
    codeLen=len("{0:#b}".format(size-1)[2:])
    i=int(a[idx:idx+codeLen],2)
    
    fin.append(d[i])
    d.append(d[i]+'1')
    d[i]=d[i]+'0'
    
    size+=1
    idx+=codeLen

fin=''.join(fin)[:8*gama]

m=open(sys.argv[2],'wb')
m.write(helper.simpleWrite(fin))