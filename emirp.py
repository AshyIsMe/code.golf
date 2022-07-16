p=lambda x:[x%i!=0 for i in range(2,x)]
[print(i)for i in range(1000)if all([i!=(r:=int(str(i)[::-1]))]+p(i)+p(r))]
