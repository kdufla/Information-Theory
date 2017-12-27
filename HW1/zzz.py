import sys
a=open(sys.argv[1]).read()
b=open(sys.argv[2]).read()

n = list(map(float, a.split()))
m = list(map(float, b.split()))

if(len(n)==len(m)):
    for x in range(len(n)):
        if(abs(n[x]-m[x])>0.000025):
            print('error', x)
