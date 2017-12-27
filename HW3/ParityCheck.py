import sys, StandardForm as s, os

def get_parity_transpose(ls,n,k):
    return [[ls[z][x] for z in range(k)] for x in range(k,n)]

def append_identity(ls):
    l=len(ls)
    for x in range(l):
        idl=[0]*l
        idl[x]=1
        ls[x]+=idl

def get_parity_ckeck(ls,n,k):
    zzz=get_parity_transpose(ls,n,k)
    append_identity(zzz)
    return zzz

def bubble(ls,cols,k):
    n=len(cols)
    swapped=True
    while(swapped):
        swapped=False
        for i in range(1,n):
            if(cols[i-1]>cols[i]):
                s.swap_col(ls,i,i-1,cols,k)
                swapped=True

def parity_check(in_file,out_file):
    temp_file='__temp__file__'
    s.standard_form(in_file,temp_file)
    a=open(temp_file,'r')
    n, k= map(int, a.readline().split())
    ls = [[int(z) for z in a.readline() if z!='\n'] for _ in range(k)]
    cols = [int(z) for z in a.readline().split()]
    a.close()
    os.remove(temp_file)
    ll=get_parity_ckeck(ls,n,k)
    bubble(ll,cols,len(ll))
    a=open(out_file,'w')
    a.write(str(len(ll[0]))+' '+str(len(ll))+'\n')
    for x in ll:
        a.write(''.join(str(z) for z in x)+'\n')
    a.close()

def main():
    parity_check(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()