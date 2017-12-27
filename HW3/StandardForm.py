import sys

def strls(ls):
    for x in ls:
        print(','.join([str(z) for z in x]))
    print()

def line_xor(ls,x,y,n):
    for i in range(n):
        ls[x][i]=ls[x][i]^ls[y][i]
        
def swap_row(ls,x,y,k):
    t=ls[x]
    ls[x]=ls[y]
    ls[y]=t
        
def swap_col(ls,x,y,cols,k):
    for i in range(k):
        t=ls[i][x]
        ls[i][x]=ls[i][y]
        ls[i][y]=t
    
    t=cols[x]
    cols[x]=cols[y]
    cols[y]=t
 
def bring_one_at(ls,x,cols,k,n):
    if(not ls[x][x]):
        i=x+1
        while(i<k and not ls[i][x]):
            i+=1
        if(i<k):
            swap_row(ls,x,i,k)
        else:
            i=x+1
            while(i<n and not ls[x][i]):
                i+=1
            swap_col(ls,x,i,cols,k)

def zeros_in_col(ls,i,n,k):
    for x in range(k):
        if(x!=i and ls[x][i]):
            line_xor(ls,x,i,n)

def standard(ls,cols,n,k):
    for x in range(k):
        bring_one_at(ls,x,cols,k,n)
        zeros_in_col(ls,x,n,k)

def standard_form(in_file,out_file):
    a=open(in_file,'r')
    n, k= map(int, a.readline().split())
    ls=[[int(z) for z in a.readline() if z!='\n'] for _ in range(k)]
    a.close()
    cols=[x+1 for x in range(n)]
    standard(ls,cols,n,k)
    a=open(out_file,'w')
    a.write(str(n)+' '+str(k)+'\n')
    for x in ls:
        a.write(''.join(str(z) for z in x)+'\n')
    a.write(' '.join(str(z) for z in cols))
    a.close()

def main():
    standard_form(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()