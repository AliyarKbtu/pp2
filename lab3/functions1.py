1
class Function():
    def __init__(self):
        pass
    def f(self):
        self.grams=int(input())
        self.ounces=self.grams*28.3495231
        print(self.ounces)
Function().f()

2
class T():
    def __init__(self):
        pass
    def temp(self):
        self.fahr=int(input())
        self.celc=(5/9)*(self.fahr-32)
        print(self.celc)
T().temp()

3
def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))

solve(35,94)

4
def is_prime(n): 
    if n <= 1: 
        return False 
    if n <= 3: 
        return True 
    if n % 2 == 0 or n % 3 == 0: 
        return False 
    i = 5 
    while i * i <= n: 
        if n % i == 0 or n % (i + 2) == 0: 
            return False 
        i += 6 
    return True 
 
def filter_prime(numbers): 
    prime_numbers = [] 
    for num in numbers: 
        if is_prime(num): 
            prime_numbers.append(num) 
    return prime_numbers 
 
numbers = [2, 3, 5, 6, 7, 8, 9, 10, 11] 
print(filter_prime(numbers))

5
def toString(List): 
    return ''.join(List) 
def permute(a,l,r): 
    if l==r: 
        print(toString(a)) 
    else: 
        for i in range(l, r+1): 
            a[l],a[i]=a[i],a[l] 
            permute(a, l+1, r) 
            a[l],a[i]=a[i],a[l] 
string=input() 
n=len(string) 
a=list(string) 
permute(a,0,n-1)

6
def reverse_sentence(sentence): 
    words = sentence.split() 
    reversed_words = ' '.join(reversed(words)) 
    return reversed_words 
 
user_input = input() 
rev_sentence = reverse_sentence(user_input) 
print(user_input +" ->", rev_sentence)

7
def has_33(nums):
    for num in nums:
        if nums[0] == nums [1] == 3 or nums[1] == nums[2] == 3:
            return True
    else:
        return False

8
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i] == 0:
            for x in range(i+1,len(nums)):
                if nums[x] == 0:
                    for y in range(x+1,len(nums)):
                        if nums[y] == 7:
                            return True
                else:
                    return False

9
import math

def sphere_volume(radius):
    return (4.0/3.0) * math.pi * (radius ** 3)

radius = int(input())
print("Volume of the sphere:", sphere_volume(radius))

10
def unique_elements(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", original_list)
print("List with unique elements:", unique_elements(original_list))

11
def is_palindrome(s):
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("A man, a plan, a canal, Panama"))  
print(is_palindrome("Not a palindrome"))

12
def histogram(int_list):
    for num in int_list:
        print('*' * num)

histogram([4, 9, 7])

13
import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 20.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {attempts} guesses!")
            break

guess_the_number()

14
import math

def sphere_volume(radius):
    '''Calculate the volume of a sphere given its radius.'''
    return (4.0/3.0) * math.pi * (radius ** 3)

def unique_elements(lst):
    '''Return a new list with unique elements of the first list.'''
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

def is_palindrome(s):
    '''Check whether a word or phrase is a palindrome.'''
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

def histogram(int_list):
    '''Print a histogram to the screen for a list of integers.'''
    for num in int_list:
        print('*' * num)









