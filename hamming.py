inp_str = list(map(int,(input("enter code : "))))  #[1,0,1,1,0,0,1]
m = len(inp_str) # 7
r = 0
#2**r >= m+r+1
for i in range(0,m):
    if((2**i)>=m+i+1):
        r=i
        break
l = m+r
redundancy_list=[]
for i in range(0,l+1):
    a = list(map(int,bin(i)[2:]))
    while(len(a)<r):
        a=[0]+a
    redundancy_list.append(a)

red_lits=[]
for i in range(0,r):
    r=[]
    for j in range(0,l+1):
        if(redundancy_list[j][-1-i]==1):
            r.append(j)
    red_lits.append(r)
print(red_lits)

code = []
k=0
for i in range(1,l+1):
    if((2**k)==i):
        code.append(-1)
        k+=1
    else:
        code.append(0)
code.reverse()
k=0
for i in range(0,l):
    if(code[i]!=-1):
        code[i]=inp_str[k]
        k+=1
code.reverse()
k=0
for i in range(0,l):
    if(code[i]==-1):
        d=0
        for j in red_lits[k]:
            if(code[j-1]!=-1):
                d+=code[j-1]
        k+=1
        d%=2
        code[i]=d
code.reverse()
print(code)
    
rec_code=list(map(int,input("enter reciver side code : ")))

rec_code.reverse()
ret=[]
for j in range(0,4):
    t = 0
    print(red_lits[j])
    for i in red_lits[j]:
        t+=rec_code[i-1]
    t%=2
    ret = [t]+ret

print(ret)


