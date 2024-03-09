#verilen bir pozitif tam sayı için fibonacci dizisinin ilk n terimini hesaplayan bir python fonksiyonu yazınız.
def fibonacci(n):
    fibo=[0,1]
    for i in range(2,n):
        next=fibo[-1]+fibo[-2]
        fibo.append(next)
    return fibo
n=22
fibo=fibonacci(n)
print(f"{fibo}")