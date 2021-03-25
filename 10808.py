#알파벳 = 26개

S=input()
al=[0 for i in range(26)]

for i in S:
    if i=='a':
        al[0]+=1
    elif i=='b':
        al[1]+=1
    elif i=='c':
        al[2]+=1
    elif i=='d':
        al[3]+=1
    elif i=='e':
        al[4]+=1
    elif i=='f':
        al[5]+=1
    elif i=='g':
        al[6]+=1
    elif i=='h':
        al[7]+=1
    elif i=='i':
        al[8]+=1
    elif i=='j':
        al[9]+=1
    elif i=='k':
        al[10]+=1
    elif i=='l':
        al[11]+=1
    elif i=='m':
        al[12]+=1
    elif i=='n':
        al[13]+=1
    elif i=='o':
        al[14]+=1
    elif i=='p':
        al[15]+=1
    elif i=='q':
        al[16]+=1
    elif i=='r':
        al[17]+=1
    elif i=='s':
        al[18]+=1
    elif i=='t':
        al[19]+=1
    elif i=='u':
        al[20]+=1
    elif i=='v':
        al[21]+=1
    elif i=='w':
        al[22]+=1
    elif i=='x':
        al[23]+=1
    elif i=='y':
        al[24]+=1
    else:
        al[25]+=1

for i in range(26):
    print(al[i],end=' ') #enterkey 없이 출력 