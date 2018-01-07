from numpy.polynomial import polynomial as pol
from itertools import permutations
import sys

def get_input(in_file,in_file2):
	a=open(in_file,'r')
	p=int(a.readline())
	n=int(a.readline())
	newp=p**n
	extender=list(map(int, a.readline().split()))
	a.close()
	a=open(in_file2,'r')
	i=int(a.readline())
	a.close()
	return (p,n,extender,i)

def trim(ls):
	maxp=0
	for i,v in enumerate(ls):
		if(v!=0):
			maxp=i
	return ls[:maxp+1]


def get_extended_cycle(p,n,extender):
	newp=p**n-1
	a=[0, 1]
	curr=[0, 1]

	alphas={0:[1],1:a}

	for x in range(2,n):
		curr=pol.polymul(curr,a)
		alphas[x]=list(map(int,curr))

	curr=list(map(lambda x: -x%p, extender[:-1]))
	curr=trim(curr)
	alphas[n]=curr

	for x in range(n+1,newp):
		curr=pol.polymul(curr,a)
		while(len(curr)>n):
			nam=int(curr[-1]%p)
			curr=list(map(lambda x: int(x)%p,pol.polyadd(list(map(lambda x: x*nam, alphas[len(curr)-1])),curr[:-1])))
		curr=list(map(lambda x: int(x)%p, curr))
		alphas[x]=list(map(int,curr))
		
	return(alphas)

def get_betas(p,n,i,alphas):
	b=alphas[i]
	curr=alphas[i]
	betas=set()
	curi=1
	bigp=p**n-1
	curr=i
	for x in range(n):
		betas.add(tuple(alphas[curr%bigp]))
		curr*=p

	return betas

def prod(ls):
	curr=[1]
	for x in ls:
		curr=pol.polymul(curr,x)
	return curr

def su(ls):
	curr=[0]
	for x in ls:
		curr=pol.polyadd(curr,x)
	return curr

def get_minimal_from_betas(alphas,betas,p,n):
	m=[0]*(len(betas)+1)
	sign = 1
	for i in range(len(betas) + 1):
		curr = set()
		for arr in permutations(betas, i):
			curr.add(tuple(sorted(arr)))
		curr=su(list(map(lambda x: prod(list(x)), curr)))
		
		while(len(curr)>n):
			nam=int(curr[-1]%p)
			curr=list(map(lambda x: int(x)%p,pol.polyadd(list(map(lambda x: x*nam,alphas[len(curr)-1])),curr[:-1])))
			curr=trim(curr)
		curr=trim(list(map(lambda x: int(x)%p,curr)))
		m[len(betas) - i] = sign * curr[0]
		sign *= -1
	return list(map(lambda x: x%p,m))

def minimal_polynomial(in_file,in_file2,output_file):
	p,n,extender,i=get_input(in_file,in_file2)
	alphas=get_extended_cycle(p,n,extender)
	betas=get_betas(p,n,i,alphas)
	m=get_minimal_from_betas(alphas,betas,p,n)
	a=open(output_file,'w')
	a.write(str(p)+'\n'+str(len(m)-1)+'\n'+' '.join(map(str,m))+'\n')


def main():
	minimal_polynomial(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
	main()
