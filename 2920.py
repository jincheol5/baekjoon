value=input().split(' ')

jud=True
if value[0]=='1':
  for i in range(len(value)):
    if (i+1)!=int(value[i]):
      jud=False
  if jud: print("ascending")
  else: print("mixed")
elif value[0]=='8':
  count=1
  for i in range(len(value)-1,0,-1):
    if int(value[i])!=count:
      
      jud=False
    count+=1
  if jud: print("descending")
  else: print("mixed")
else: print('mixed')
