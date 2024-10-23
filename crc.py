inp_code = list(map(int,list(input())))
divisor = list(map(int,list(input())))

inp=[]
for i in range(0,len(inp_code)):
    inp.append(inp_code[i])
print("input : ",inp_code)
print("divisor: ",divisor)

print("\n")
for i in range(0,len(divisor)-1):
    inp.append(0)

while(len(inp)>len(divisor)-1):
    if(inp[0]==1):
        for i in range(0,len(divisor)):
            inp[i]+=divisor[i]
            inp[i]%=2
    inp=inp[1:]

print(inp)

inp_code+=inp
print(inp_code)

reciver = list(map(int,list(input())))
rec = []
for i in range(0,len(reciver)):
    rec.append(reciver[i])
print(rec)
while(len(rec)>len(divisor)-1):
    if(rec[0]==1):
        for i in range(0,len(divisor)):
            rec[i]+=divisor[i]
            rec[i]%=2
    rec=rec[1:]

print(rec)
    