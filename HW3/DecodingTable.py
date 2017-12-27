import sys, itertools, ParityCheck, helper, os,StandardForm

# code from stackoveflow. itertools.permutations would be the same but slower
#begin
class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1
#end 

def mmult(p,err,k):
    for i in range(k):
        yield str(sum(p[i][r] for r in err)%2)

def error_idx(t):
    for i in range(len(t)):
        if t[i]=='1':
            yield i

def sindrome(p,e,k):
    return ''.join(mmult(p,list(error_idx(e)),k))

def error_perm(e,n):
    for err_count in range(1,e+1):
        for perm in perm_unique(['1']*err_count+['0']*(n-err_count)):
            yield perm

def generate_errors(e,n):
    return list(error_perm(e,n))

def s_and_e(p,e,n,k):
    for x in generate_errors(e,n):
        yield sindrome(p,x,k)+''.join(x)

def getGama(integer):
    num="{0:#b}".format(integer)[3:]
    return '0'*len(num)+'1'+num

def parity_to_bin(n,k,p):
    return getGama(n)+getGama(k)+''.join(''.join(str(p[i][j]) for j in range(n)) for i in range(k))

def decoding_table(in_file, in_file_1, out_file):
    temp_file='__temp__file__'
    ParityCheck.parity_check(in_file,temp_file)
    a=open(temp_file,'r')
    n, k= map(int, a.readline().split())
    p = [[int(z) for z in a.readline() if z!='\n'] for _ in range(k)]
    a.close()
    os.remove(temp_file)
    a=open(in_file_1,'r')
    max_e=int(a.read())
    a.close
    a=open(out_file,'wb')
    a.write(helper.completeWrite(parity_to_bin(n,k,p)+''.join(s_and_e(p,max_e,n,k))))

def main():
    decoding_table(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()