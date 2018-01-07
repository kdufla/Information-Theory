from collections import deque
from numpy import matmul,transpose
from numpy.polynomial import polynomial as p
import sys

def decode(in_file, in_file2, out_file):
	a=open(in_file,'r')
	base=int(a.readline())
	n=int(a.readline())
	poly=list(map(int, a.readline().split()))
	a.close()

	maxp=0
	for i,v in enumerate(poly):
		if(v==1):
			maxp=i

	a=open(in_file2,'r')
	data_len=int(a.readline())
	data=list(map(int, a.readline().split()))
	a.close()

	decoded = []
	data_idx = 0
	while data_idx < data_len:
		cur_data = data[data_idx: data_idx + n]
		dec=list(map(lambda x: int(x%base),p.polydiv(list(map(lambda x: x%base,cur_data)),list(map(lambda x: x%base,poly)))[0]))
		decoded+=dec+(n-maxp-len(dec))*[0]
		#print(dec+(n-maxp-len(dec))*[0])
		data_idx += n

	a=open(out_file,'w')
	a.write(str(len(decoded))+'\n'+' '.join(map(str,decoded))+'\n')
	print(decoded)

def main():
	decode(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
	main()