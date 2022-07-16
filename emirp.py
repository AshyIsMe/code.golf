p=lambda x:all([not x%i==0 for i in range(2,x)])
r=lambda x:int(str(x)[::-1])
[print(i)for i in range(1000)if p(i)and i!=r(i)and p(r(i))]
