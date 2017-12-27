from numpy import unpackbits, packbits

def translate(a):
    for x in a:
        if x=='0':
            yield 0
        else:
            yield 1

def simpleRead(input,outputFile):
    b=open(outputFile, 'wb')
    for x in unpackbits(bytearray(input)):
        b.write(str(x))

def completeRead(input,outputFile):
    b=open(outputFile, 'wb')
    a=unpackbits(bytearray(input))
    for x in a[:len(a)-1-list(a[::-1]).index(1)]:
        b.write(str(x))

def simpleWrite(input, outputFile):
    b=open(outputFile, 'wb')
    b.write(packbits(list(translate(input))))

def completeWrite(input, outputFile):
    input=input+'1'+ ('' if len(input)%8==7 else '0'*(8-((len(input)+1)%8)))
    b=open(outputFile, 'wb')
    b.write(packbits(list(translate(input))))

def getHuffmanCoding(leng,ls):
    q=[]
    for x in range(len(ls)):
        q.append((ls[x],x))
    q.sort(reverse=True)

    while len(q)>1:
        fi=q.pop()
        se=q.pop()
        q.append((fi[0]+se[0],(fi,se)))
        try:
            q.sort(reverse=True)    
        except:
            pass
    def build(node,currCode, code):
        if type(node[1]) is int:
            code[node[1]]=currCode
        else:
            build(node[1][0],currCode+'0', code)
            build(node[1][1],currCode+'1', code)

    code=[0]*leng
    build(q.pop(),'',code)
    return [int(x) for x in code]

def buildCodeDictionary(code):
    alp=' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
    dic={}
    for x in range(34):
        dic[alp[x]]=code[x]
    return dic

def buildAlpDictionary(alp):
    code=' აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
    dic={}
    for x in range(34):
        dic[alp[x]]=code[x]
    return dic