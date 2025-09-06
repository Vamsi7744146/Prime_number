#write a program to print first 10 print numbers
n=2
target=10
c=0
while c<target:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            c+=1

    n+=1
