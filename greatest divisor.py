# greatest-divisor
i,j=map(int,input().split())
p=list()
for o in range(1,1000):
    if i%o==0:
        if j%o==0:
            p.append(o)
print(max(p))
            
