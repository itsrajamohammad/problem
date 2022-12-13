cockroach1=0
cockroach2=0
t=0
d=100
while True:
    #t is time
    t+=1
    #a steps forward 1step per sec n reverse 2 step for every 10 sec
    if t%10==0:
        cockroach1-=2
        cockroach1+=1
    else:        
        cockroach1+=1
     #b steps forward 2step per sec n reverse 1 step for every 5 sec    
    if t%5==0:
        cockroach2-=1
        cockroach2+=2
    else:
        cockroach2+=2
    #to calc exact time for distance
    if cockroach1+cockroach2>d:
        t-=1
        cockroach1-=1
        cockroach2-=2
        t+=(d-cockroach1-cockroach2)/3
        break
print(t)