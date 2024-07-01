def power(x,n):
#base case: anynumber to the power of 0 is 1
    if n == 0:
        return 1
 #if n is negative, convert it into positive   
    if n < 0:
        x = 1/x
        n = -n
#recursive case
    half = power(x, n//2)

#if n is even 
    if n % 2 == 0:
        return half * half 
    else:
#if n is odd
        return half *half *x

#example usage
x = 2.10000
n= 3
print(f"{x}^{n} = {power(x,n)}")