import sys
from collections import deque

#1번 톱니 : 2오 자리 
#2,3번 톱니 : 2오,6왼자리
#4번 톱니 : 6왼 자리
#N극이 0 S극이 1
class gear:
  def __init__(self):
    #마주보는 톱니 극 같을 경우 0 아닐경우 1
    self.k1=-1 #1-2
    self.k2=-1 #2-3
    self.k3=-1 #3-4
    
    
    
    self.gear=[] #초기 톱니바퀴 정보 저장
    self.gear_score=0 #톱니바퀴 점수 저장 
    
  def jud_gear(self): #각 마주보는 톱니의 극이 같은지 판단 
    if self.gear[0][2]!=self.gear[1][6]: self.k1=1
    else: self.k1=0
    
    if self.gear[1][2]!=self.gear[2][6]: self.k2=1
    else: self.k2=0
    
    if self.gear[2][2]!=self.gear[3][6]: self.k3=1
    else: self.k3=0
  
  def jud_score(self): #회전 끝난 후 점수 계한하여 출력
    if self.gear[0][0]==1: self.gear_score+=1
    if self.gear[1][0]==1: self.gear_score+=2
    if self.gear[2][0]==1: self.gear_score+=4
    if self.gear[3][0]==1: self.gear_score+=8
      
    return self.gear_score
  
  def turn_gear(self,num,k): #톱니 회전시키기
    
    deq=deque(self.gear[num-1])
    
    if k==-1: #반시계방향
      x=deq.popleft()
      deq.append(x)
    if k==1: #시계방향
      x=deq.pop()
      deq.appendleft(x)
      
    self.gear[num-1]=list(deq)
      
    
    
  def turn(self,num,k): #회전
    
    self.jud_gear()
    
    if num==1:
      self.turn_gear(num,k)
      if self.k1==1: 
        self.turn_gear(2,-k)
        if self.k2==1: 
          self.turn_gear(3,k)
          if self.k3==1: 
            self.turn_gear(4,-k)
        
        
    if num==2:
      self.turn_gear(num,k)
      if self.k1==1: 
        self.turn_gear(1,-k)
      if self.k2==1: 
        self.turn_gear(3,-k)
        if self.k3==1: 
          self.turn_gear(4,k)
      
      
    if num==3:
      self.turn_gear(num,k)
      if self.k3==1: 
        self.turn_gear(4,-k)
      if self.k2==1: 
        self.turn_gear(2,-k)
        if self.k1==1: 
          self.turn_gear(1,k)
      
      
    if num==4:
      self.turn_gear(num,k)
      if self.k3==1: 
        self.turn_gear(3,-k)
        if self.k2==1: 
          self.turn_gear(2,k)
          if self.k1==1: 
            self.turn_gear(1,-k)
      
    
    
    
    
mygear=gear() #톱니 객체 생성

for i in range(4):
  s_list=[]
  s=input()
  for j in s:
    s_list.append(int(j))
  mygear.gear.append(s_list)
  



K=int(input()) #회전횟수 

for i in range(K):
  num_gear,turn_gear=map(int,sys.stdin.readline().split())
  mygear.turn(num_gear,turn_gear)


print(mygear.jud_score())
  
    