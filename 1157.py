s=input().upper()
deleted_s=list(set(s)) #s에서 중복값 제거된 s 
c_list=[]
for i in deleted_s: c_list.append(s.count(i))
if c_list.count(max(c_list))>1: print("?")
else:
  index=c_list.index(max(c_list)) 
  print(deleted_s[index])