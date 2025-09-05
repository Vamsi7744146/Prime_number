#write a program to print only 10th prime number  
n=2
c=0
while c<10:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            c+=1
            if c==10:
                print(n)
    n+=1            