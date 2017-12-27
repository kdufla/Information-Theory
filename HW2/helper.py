from numpy import packbits

def translate(a):
    for x in a:
        if x=='0':
            yield 0
        else:
            yield 1

def simpleRead(input):
    return ''.join([bin(i)[2:].zfill(8) for i in input])

def completeRead(input):
    return ''.join([bin(i)[2:].zfill(8) for i in input]).rsplit('1', 1)[0]
    
def simpleWrite(input):
    return packbits(list(translate(input)))

def completeWrite(input):
    input=input+'1'+ ('' if len(input)%8==7 else '0'*(8-((len(input)+1)%8)))
    return packbits(list(translate(input)))
