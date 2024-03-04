#task1
def multiply_list(numbers):
    sum=1
    for x in numbers:
        sum=sum*x
    return sum
a=list(map(int,input().split()))
print(multiply_list(a))

#task2
def count_letters(s):
    uppersum=0
    lowersum=0
    for x in s:
        if x.islower():
            lowersum+=1
        elif x.isupper():
            uppersum+=1
    return uppersum, lowersum
string=input()
print(count_letters(string))

#task3
def palindrome(s):
    rev=s[::-1]
    if rev==s:
        return True
    else:
        return False
string=input()
print(palindrome(string))

#task4
import time
import math
def f(a,b):
    seconds=b/1000
    time.sleep(seconds)
    x=math.sqrt(a)
    return x

num=int(input())
milliseconds=int(input())
print("Square root of",num,"after",milliseconds,"is",f(num,milliseconds))

#task5
def tuples(t):
    return all(t)

a=tuple(map(bool,input().split()))
print(tuples(a))

