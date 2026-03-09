

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1) * n
    

n=int(input("Give a number n: "))

f=factorial(n)

print(f"Factorial of {n} is {f}")
