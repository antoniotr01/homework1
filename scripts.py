#Say "Hello, World!" With Python
print("Hello, World!")

#List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n ])

#sWAP cASE
def swap_case(s):
 return ''.join([t.lower() if t.isupper() else t.upper() for t in s]) 

#Introduction to Sets
def average(array):
   a=set(array)
   return round(sum(a)/len(a),3)

#Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if (n%2 !=0):
    print ('Weird')
elif (n<6 and n>1):
    print ('Not Weird')
elif (n>5 and n<21):
    print ('Weird')
else:
     print ('Not Weird')

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b) 
print (a-b)
print(a*b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)

#Loops
if __name__ == '__main__':
    n = int(input())
a=set(range(n))
for i in a:
    print (i**2)

#Write a function
def is_leap(year):
    leap = False
    
    if (year%4==0 and year%100!=0):
        leap = True
    elif (year%4==0 and year%100==0 and  year%400==0):
        leap = True
    
    return leap
    
#Print Function
if __name__ == '__main__':
    n = int(input())
s=set(range(1,n+1))
a=''
for i in s :
        a+=str(i)
print(a)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b = list(arr)
    a = []
    for i in b:
        if( i != max(b)):
            a.append(i) 
    print(max(a))
    
#Nested Lists
if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name,score])
b = set([score for _, score in a])    
c = []
for i in b:
    if (i!=min(b)):
        c.append(i)
seclow = min(c)    
names = [name for name,score in a if score == seclow] 
for name in sorted(names):
    print(name)
    
#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
a = len(student_marks[query_name])
b = sum(student_marks[query_name]) 
print ("{:0.2f}".format(b/a))

#Concatenate
import numpy as np
n, m, p = map(int, input().split())
a=[]
b=[]
for _ in range(n):
    a.append(np.array(list(map(int, input().split()))))
for _ in range(m):
    b.append(np.array(list(map(int, input().split()))))
print(np.concatenate((a, b), axis=0))

#Zeros and Ones
import numpy
n=list(map(int,input().split()))
print(numpy.zeros(n, int), numpy.ones(n, int), sep= "\n")

#Lists
if __name__ == '__main__':
    N = int(input())
    result =[]
for i in range(N):
    imp = input().split()
    if imp[0] == "insert" :
        result.insert(int(imp[1]), int(imp[2]))
    elif imp[0] == "append" :
        result.append(int(imp[1]))
    elif imp[0] == "remove":
        result.remove(int(imp[1]))
    elif imp[0] == "sort" :
        result.sort()
    elif imp[0] == "pop":
        result.pop()
    elif imp[0] == "reverse":
        result.reverse()
    else:
        print(result)
        
#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    i = 0
    m = max(candles)
    for j in range(len(candles)):
        if (candles[j] == m):
            i+=1
    return i
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if (v1-v2==0):
        return 'NO'
    elif ((x1-x2)/(v2-v1)%1==0 and (x1-x2)/(v2-v1)>=0):
        return 'YES'
    else:
        return 'NO'
                                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
    
#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    a=2
    b=2
    for i in range(n-1):
        a= (a*3)/2-(((a*3)/2)%1) 
        b=b+a
    return int(b)       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    y=list((str(     sum([int(i) for i in list((n)) ])*k)))
    a=11
    while (a>=10):
        a=sum([int(i) for i in y ])
        y=list((str(a)))
    return a    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    a=arr[n-1]
    for i in range(n-1, -1, -1):
        if (a<arr[i-1] and i>=1):
            arr[i]=arr[i-1]
            print(" ".join(str(x) for x in arr))
        else:
            arr[i]=a
            print(" ".join(str(x) for x in arr))    
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    
#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1,n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)    
