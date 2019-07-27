v,zi=map(str,input().split())
niran=0
if len(x)>len(y):
  v,zi=zi,v
i=0
while i<len(v):
  niran+=(ord(y[i])-ord(v[i]))
  i+=1
for i in range(i,len(y)):
  niran+=ord(y[i])-ord('a')+1
print(niran)
