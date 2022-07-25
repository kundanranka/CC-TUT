n=int(input("Enter the n value :"))
i=0
for j in range(1,1000):
    if j%2==0:
        print(j)
        i+=1
    if i==n:
        break
