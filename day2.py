#print hello world
if __name__ == '__main__':
    print("Hello, World!")
#python if else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n%2==0 and n in range(2,6):
        print("Not Weird")
    elif n%2==0 and n in range(6,21):
        print("Weird")
    else:
        print('Not Weird')
#arithmetic operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
#Divison 
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
#loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
#write a function
def is_leap(year):
    leap = False
    if year%400==0 or (year%4==0 and year%100!=0):
        leap=True
    
    return leap

year = int(input())
print(is_leap(year))
#print function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')
