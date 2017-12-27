import sys,helper, DecodingTable

def xsor_and(g,m,n,k):
    for i in range(n):
        a=0
        for j in range(k):
            a= a^(g[j][i]&int(m[j]))
        yield str(a)

def get_message(g,data,n,k):
    for x in range(0,len(data),k):
        yield ''.join(xsor_and(g,data[x:x+k],n,k))

def encode(in_file, in_file_1, out_file):
    in_file=sys.argv[1]
    a=open(in_file,'r')
    n, k= map(int, a.readline().split())
    g=[[int(z) for z in a.readline() if z!='\n'] for _ in range(k)]
    a.close()
    a=open(sys.argv[2],'rb')
    data=helper.simpleRead(a.read())
    a.close()
    a=open(out_file,'wb')
    a.write(helper.completeWrite(''.join(get_message(g,data,n,k))))

def main():
    encode(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()