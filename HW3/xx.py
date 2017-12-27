import os,helper


for i in range(1,7):
    #os.system('python3 Encode.py D/00'+str(i)+'.code D/00'+str(i)+'.dat x')
    #print()
    #os.system('diff x D/00'+str(i)+'.ans -s')
    os.system('python3 DecodingTable.py C/00'+str(i)+'.dat C/00'+str(i)+'.num x')
    os.system('python3 Decode.py x E/00'+str(i)+'.dat z')
    os.system('diff z E/00'+str(i)+'.ans -s')

'''
a=open('E/001.ans','rb')
x=helper.completeRead(a.read())
a.close()
print(x)
a=open('z','rb')
y=helper.completeRead(a.read())
a.close()
print(y)
a=open('E/001.dat','rb')
z=helper.completeRead(a.read())
a.close()
print(z)
''
def idxs():
    for i in range(n):
        if(x[i]!=y[i]):
            yield i%7

def idxss():
    for i in range(n):
        if(x[i]!=y[i]):
            yield int(i/7)

print(list(idxs()))
print(list(idxss()))
'''
