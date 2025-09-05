#write program to check the given number is prime or not
n=int(input())
if n>1:
    i=2
    while i<=n//2:
        if n%i==0:
            print('n is not prime')
            break
        i+=1
    else:
        print('n is prime')
else:
    print('n is not prime')