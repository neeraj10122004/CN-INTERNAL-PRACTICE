
divisor = list(map(int,list(input("enter the divisor : "))))

dataword = list(map(int,list(input("enter the data word : "))))

data = []
for i in dataword :
    data.append(i)
for i in range(0,len(divisor)-1):
    data.append(0)

print("divisor : ",divisor)
print("original data word : ",dataword)
print("data word after appending zeros : ",data)

while (len(data)>len(divisor)-1):
    if (data[0]==1) :
        for i in range(0,len(divisor)):
            data[i]=data[i]+divisor[i]
            data[i]%=2
    data=data[1:]

print("redundancy : ",data)

dataword = dataword + data

print("transmitting frame : ",dataword,end='\n')

reciver = list(map(int,list(input("enter the reciver side input : "))))

rec = []
for i in reciver :
    rec.append(i)

while(len(rec)>len(divisor)-1):
    if(rec[0]==1):
        for i in range(0,len(divisor)):
            rec[i]=rec[i]+divisor[i]
            rec[i]%=2
    rec=rec[1:]

print("reminder : ",rec)

if sum(rec)==0 :
    print("no error")
else :
    print("error at reciver side\n")
    print(reciver)