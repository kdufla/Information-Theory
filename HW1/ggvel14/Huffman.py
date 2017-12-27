import sys, helper
a=open(sys.argv[1])
b=open(sys.argv[2], 'w')

leng=int(a.readline())
ls=list(map(float,a.readline().split()))
z=helper.getHuffmanCoding(leng,ls)

for x in z:
        b.write(str(x) + "\n")

