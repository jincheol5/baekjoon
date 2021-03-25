s=input()
count=0
rc=0
jud=0
ss=''
for i in s:
    rc+=1
    ss+=i
    count+=1
    if count==10:
        jud=1
        print(ss)
        ss=''
        count=0
    if rc==len(s):
        print(ss)
        break

