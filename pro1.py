niran=int(input())
vizh=[]
for x in range(0,niran):
 viji=input()
 vizh.append(viji)
new=[]
for x in zip(*vizh):
 if(x.count(x[0])==len(x)):
  new.append(x[0])
 else:
  break
print(''.join(new))
