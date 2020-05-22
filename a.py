i=0
n=8
p=1000
q=1000
avarde=5300
sod=0
mojodi=0
k=0
d=2
import random
for y in range(p):
           n=8
           mojodi=avarde
           bet=1
           for x in range(q):
               if bet>mojodi:
                  k+=1
                  break
               i=random.random()
               if (i<=0.5250):
                  mojodi-=bet
                  bet=d*bet
                  n=0
               elif n==8:
                     mojodi+=bet
               elif n!=8:
                      if n==0:
                         n=8
                         mojodi+=bet
                         bet=1
                      else:
                         mojodi+=bet
                         bet=d*bet
                         n+=1
               if (x==q-1):
                   sod+=mojodi-avarde
                  # print(i)
                  # print(sod)
                   #print(y)
                   #gg=input()
if ((p-k)!=0):
  print('sod',sod/(p-k))
else:
  print('sod',0)
print('tedad begayi',k)
print('chance% bakht',k/p*100)
if (((p-k)!=0) and (k!=0)):
  print('factor',((1-k/p)/(k/p))*((sod/(p-k))/avarde))
else:
  print('factor kamelan khob va ghatei')       
                    
                         
               


