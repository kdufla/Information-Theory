import sys,helper,time

a=helper.simpleRead(open(sys.argv[1],'rb').read())

def getGama(file):
    num="{0:#b}".format(int(len(file)/8))[3:]
    return '0'*len(num)+'1'+num

finalAns=[getGama(a)]

d={}
d['0']=0
d['1']=1
l=1
idx=0
size=2
while(True):
    if a[idx:idx+l] in d:
        if(idx+len(a[idx:idx+l])>=len(a)):
            st=a[idx:idx+l]
            #print(st)
            codeLen=len("{0:#b}".format(size-1)[2:])
            code="{0:#b}".format(d[st])[2:]
            code='0'*(codeLen-len(code))+code
            finalAns.append(code)
            break
        l+=1
    else:
        st=a[idx:idx+l-1]
        d[st+'0']=d[st]
        d[st+'1']=size

        codeLen=len("{0:#b}".format(size-1)[2:])
        code="{0:#b}".format(d[st])[2:]
        code='0'*(codeLen-len(code))+code
        finalAns.append(code)

        size+=1
        l=1
        idx+=len(st)

m=open(sys.argv[2],'wb')
m.write(helper.completeWrite(''.join(finalAns)))
