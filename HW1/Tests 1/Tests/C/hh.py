import sys
a=open(sys.argv[1]).read()
b=open(sys.argv[2], 'w')

nums=list(map(int,a.split()))
saveCopyOfNums=nums[:]

def inc(currCode):
    currCode=list(currCode)
    idx=len(currCode)-1
    while currCode[idx]=='1':
        currCode[idx]='0'
        idx-=1
    currCode[idx]='1'
    return ''.join(currCode)

if sum([2**-x for x in nums])<=1:
    codes={}
    currCode='0'
    for l in sorted(nums):
        currCode+='0'*(l-len(currCode))
        codes.setdefault(len(currCode),[]).append(currCode)
        currCode=inc(currCode)
    for x in nums:
        b.write(str(codes[x].pop()) + "\n")
