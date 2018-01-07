from collections import deque
from numpy import matmul
import sys

def encode(in_file, in_file2, out_file):
	a=open(in_file,'r')
	base=int(a.readline())
	n=int(a.readline())
	poly_generator=deque(list(map(int, a.readline().split())))
	a.close()

	generator=[list(poly_generator)]

	while(poly_generator[-1]==0):
		poly_generator.rotate(1)
		generator.append(list(poly_generator))

	a=open(in_file2,'r')
	data_len=int(a.readline())
	data=list(map(lambda x: int(x), a.readline().split()))
	a.close()

	cc=len(generator)
	ll=[]
	for i in range(int(data_len/cc)):
		ll+=list(map(lambda x: x%base, matmul(data[cc*i:cc*(i+1)],generator)))

	a=open(out_file,'w')
	a.write(str(len(ll))+'\n'+' '.join(map(str, ll))+'\n')

def main():
	encode(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
	main()