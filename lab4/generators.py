#task1
def gen_square(n):
    for i in range(1, n + 1):
        yield i**2

n=int(input())
for x in gen_square(n):
    print(x,end=" ")

#task2
def even_comma(n):
    for i in range(0,n+1,2):
        yield i
n=int(input())
for x in even_comma(n):
    if x<n-1:
        print(x,end=",")
    else:
        print(x)

#task3
def divby3and4(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for x in divby3and4(n):
    print(x,end=" ")

#task4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
for x in squares(a,b):
    print(x, end=" ")

#task5
def rev(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
for x in rev(n):
    print(x,end=" ")


