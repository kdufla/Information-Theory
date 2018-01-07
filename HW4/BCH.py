from numpy.polynomial import polynomial as pol
from MinimalPolynomial import minimal_polynomial as mp, get_input,prod
import sys

#input_file='Tests/E/001.dat'
#input_file2='Tests/E/001.dst'



#print(p,n,extender,i)

def prep_file(st,wst):
    a=open(st,'w')
    a.write(wst)
    a.close()
    return st

def bch(input_file,input_file2,out_file):
    p,n,extender,i=get_input(input_file,input_file2)

    temp_file='temp'

    minps=set()
    for x in range(1,i):
        #print('getmp: ',input_file,prep_file('inp'+str(x),str(x)),temp_file)
        mp(input_file,prep_file('inp'+str(x),str(x)),temp_file)
        _,_,minp,_=get_input(temp_file,input_file2)
        minps.add(tuple(minp))

    ans=list(map(lambda x: int(x%p),prod(minps)))
    maxlen=p**n-1
    ans=ans+(maxlen-len(ans))*[0]

    a=open(out_file,'w')
    a.write(str(p)+'\n'+str(len(ans))+'\n'+' '.join(map(str, ans))+'\n')    
    a.close()

def main():
	bch(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
	main()
