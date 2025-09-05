#write a program to print prime numbers in the given range
LL=int(input())
UL=int(input())

for num in range(LL,UL+1):
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
               
                break
        else:
            
            print(num)