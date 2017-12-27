import helper,sys,StandardForm, numpy as np

def get_from_gama(gamaStr,i):
    idx=0
    while(gamaStr[idx+i]=='0'):
        idx+=1
    return int(str(gamaStr[idx+i:2*idx+1+i]),2)

def get_gama_code_len(gamaStr,i):
    idx=0
    while(gamaStr[idx+i]=='0'):
        idx+=1
    return idx*2+1

def get_n_k_of(data):    
    n=get_from_gama(data,0)
    of=get_gama_code_len(data,0)
    k=get_from_gama(data,of)
    of+=get_gama_code_len(data,of)
    return (n,k,of)

def error_idx(t):
    for i in range(len(t)):
        if t[i]==1:
            yield i

def error_idx2(t):
    for i in range(len(t)):
        if t[i]==1:
            yield i

def mmult(p,m,k):
    for i in range(k):
        yield str(sum(p[i][r] for r in error_idx(m))%2)

def build_dictionary(data,n,k,of):
    dic={}
    for i in range(of,len(data),k+n):
        dic[data[i:i+k]]=data[i+k:i+k+n]
    return dic

def get_p(data,of,n,k):
    for i in range(0,k*n,n):
        yield [int(data[of+i+x]) for x in range(n)]

def get_p_ls(data,of,n,k):
    return list(get_p(data,of,n,k))

def flip(code,l,of):
    for i in l:
        code[of+i]^=1

def correction(code,dict, n, k,p):
    cc=code[:]
    zero=k*'0'
    for i in range(0,len(code),n):
        sindrome=''.join(mmult(p,code[i:i+n],k))
        if(sindrome!=zero):
            err=dict[sindrome]
            erors=error_idx2([int(x) for x in err])
            flip(code, error_idx2([int(x) for x in err]), i)
    
def decode(in_file, in_file_1, out_file):
    a=open(in_file,'rb')
    data=helper.completeRead(a.read())
    a.close()
    a=open(in_file_1,'rb')
    code=[int(x) for x in helper.completeRead(a.read())]
    a.close()
    n,k,of=get_n_k_of(data)
    p=list(get_p_ls(data,of,n,k))
    of+=n*k
    dict=build_dictionary(data,n,k,of)
    correction(code,dict,n,k,p)
    a=open(out_file,'wb')
    a.write(helper.completeWrite(''.join(str(x) for x in code)))
    a.close()
    
def main():
    decode(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()