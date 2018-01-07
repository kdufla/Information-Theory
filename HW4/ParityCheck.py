from numpy.polynomial import polynomial as p
import sys

def parity(in_file, out_file):
	a=open(in_file,'r')
	base=int(a.readline())
	n=int(a.readline())
	dividend=[base-1]+[0]*(n-1)+[1]
	divisor=list(map(int, a.readline().split()))
	a.close()

	result=p.polydiv(dividend,divisor)
	q=list(map(lambda x: int(x%base),result[0]))+(n-len(result[0]))*[0]
	r=list(map(lambda x: int(x%base),result[1]))

	a=open(out_file,'w')
	if(sum(r)>0):
		a.write('NO\n')
	else:
		a.write('YES\n')
		a.write(' '.join(map(str,q))+'\n')
	a.close()


def main():
    parity(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()