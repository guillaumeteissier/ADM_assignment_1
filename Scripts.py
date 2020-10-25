# SECTION: Introduction

# Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else
if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n in list(range(2,6)):
    print("Not Weird")
elif n in list(range(6,21)):
    print("Weird")
elif n > 20:
    print("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())

for i in range(0,n):
    print(i**2)

# Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        else:
            leap = True    

    else:
        leap = False    

    return leap

year = int(input())
print(is_leap(year))

# Print Function
if __name__ == '__main__':
    n = int(input())

list_digits = list(range(1,n+1))
list_strings = []

for i in list_digits:
    list_strings.append(str(i))

print("".join(list_strings))

# SECTION: Basic Data Types

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i + j + k != n ])

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

print(sorted(set(arr))[-2])

# Nested Lists
test_list = []
for x in range(int(input())):
    test_list.append([input(), float(input())])

grades = []
for grade in test_list:
    grades.append(grade[1])

second = sorted(grades)[1]

sorted_names = []
for x in test_list:
    if second == x[1]:
        sorted_names.append(x[0])

sorted_names = sorted(sorted_names)
for x in sorted_names:
    print(x)

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

total_grade =sum([x for name_1, grade in student_marks.items() for x in grade if query_name == name_1])

average = total_grade/3
print("%.2f"%(average))

# Lists
if __name__ == '__main__':
    N = int(input())

test_list = []
for _ in range(N):
    formated = input().split()
    test_list.append(formated)

empty_list = []

for x in test_list:
    if x[0] in ["insert"]:
        empty_list.insert(int(x[1]),int(x[2]))
    elif x[0] in ["append","remove"]:
        exec("empty_list."+x[0]+"(int(x[1]))")
    elif x[0] in ["sort","pop","reverse"]:
        exec("empty_list."+x[0]+"()")
    else: 
        print(empty_list)

# Tuples
if __name__ == '__main__':
    n = int(input())
    the_list = map(int, input().split())

print(hash(tuple(list(the_list))))

# sWAP cASE
def swap_case(s):
    the_string = "".join([x.lower() if x.isupper() else x.upper() for x in s])
    return the_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# String Split and Join
def split_and_join(line):
    # write your code here
    test = line.split(" ")
    test = "-".join(test)
    return test

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
def print_full_name(a, b):
    print("Hello "+a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# SECTION: Strings
# Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Find a string
def count_substring(string, sub_string):
    counts = 0
    for x in range(0, len(string)):
        if string[x:x+len(sub_string)] == sub_string:
            counts +=1
    return counts

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
# String Validators
if __name__ == '__main__':
    s = input()

print(any(x.isalnum() for x in s))
print(any(x.isalpha() for x in s))
print(any(x.isdigit() for x in s))
print(any(x.islower() for x in s))
print(any(x.isupper() for x in s))

# Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone - yass
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars- I am good for this one
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
# Text Wrap
import textwrap

def wrap(string, max_width):
    # Thank you lord for textwrap
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# String Formatting
def print_formatted(number):
    for x in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(x, width=len("{0:b}".format(n))))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
#Capitalize!
def solve(s):
    # thank you map function, # thank you split function we could not have done it without you
    test = " ".join(map(str.capitalize, s.split(" ")))
    return test

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    #it is guaranteed that n is a multiple of k
    #We can split s into n/k subsegments where each subsegment, Ti, consists of a contiguous block of k characters in s. 
    # first step - get the subsegments
    for x in range(0, len(string), k):
        chunkies = (string[0+x:k+x])
        clean_chunks = []
        for letter in chunkies:
            if letter not in clean_chunks:
                clean_chunks.append(letter)
        print("".join(clean_chunks))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# The Minion Game
# Did not look at the solution on hackerrank but there were solutions on the web. 
def minion_game(string):

    vowel = "AEIOU"

    kevin = 0
    stuart = 0
    for x in range(len(s)):
        if s[x] in vowel:
            kevin += (len(s)-x)
        else:
            stuart += (len(s)-x)


    if kevin == stuart:
        print("Draw")
    elif kevin < stuart:
        print("Stuart " + str(stuart))
    elif kevin > stuart:
        print("Kevin " + str(kevin))
        
# SECTION: Sets

# Introduction to Sets
def average(array):
    # your code goes here
    return (sum(set(array))/len(set(array)))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# No Idea!
# okey it is a problem of counting unions and intersections. 
# my guess is that there will be a runtime error if it is not simpl enough ffs
# FUCK YOU TIMEOUT
# first let's get the array into a set
# actually no that fucks my shit. don't do that
a = input()
set_1 = list(map(int, input().split()))
set_happy = set(map(int, input().split()))
set_sad = set(map(int, input().split()))
# Now i want the intersection between the array and the set that add points
count_happy = sum([1 for x in set_1 if x in set_happy])
count_sad = sum([1 for x in set_1 if x in set_sad])
print(count_happy-count_sad)

# Symmetric Difference
input()
set_1=set(map(int, ((input().split()))))
input()
set_2=set(map(int, ((input().split()))))
test_inter = sorted(set_1.union(set_2) - set_1.intersection(set_2))

for x in test_inter:
    print(x)

# Set .add()
n = int(input())
stamps = set()
for i in range(n):
    stamps.add(input())
print(len(stamps))

# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
# freaking hfhfhfdhd input
N=int(input())
for i in range(N) :
    command=input().split()
    if command[0]=="pop" :
        s.pop()
    elif command[0]=="remove" :
        s.remove(int(command[1]))
    elif command[0]=="discard" :
        s.discard(int(command[1]))
print(sum(s))

#Set .union() Operation
a = (input()).split()
b = set((input()).split())
c = (input()).split()
d = set((input()).split())
print(len(b.union(d)))

#Set .intersection() Operation
a = input().split()
b = set(input().split())
c = input().split()
d = set(input().split())

print(len(b.intersection(d)))

#Set .difference() Operation
a = input().split()
b = set(input().split())
c = input().split()
d = set(input().split())

print(len(b.difference(d)))

#Set Mutations
a = int(input())
set_1 = set(map(int, input().split()))
N = int(input())

for x in range(N):
    cmd,x = input().split()
    set_2 = set(map(int, input().split()))
    if(cmd == "intersection_update"):
        set_1.intersection_update(set_2)
    elif(cmd == "update"):
        set_1.update(set_2)
    elif(cmd == "symmetric_difference_update"):
        set_1.symmetric_difference_update(set_2)
    elif(cmd == "difference_update"):
        set_1.difference_update(set_2)

print(sum(set_1))

# Check Subset
for x in range(int(input())):
    a = input() 
    b = set(input().split()) 
    c = input() 
    d = set(input().split())
    print(b.issubset(d))

# SECTION: Collections

# collections.Counter()
# I swear this would have been the most useful package in the previous exercises.
#https://www.youtube.com/watch?v=ixr5GSUWwEw
# First the count of shoes
from collections import Counter
a = input()
b = Counter(map(int,input().split()))
c = int(input())
# done
monayyy = 0
for x in range(c):
    # at this point it is almost copy pasta for this one
    size, price = (map(int, input().split()))
    #print(size)
    #print(price)
    # okey you got the price and size, know you need to check if the size is in b and if it is make monay AND substract the sell and if it is not ...do nothing i guess
    if size in b:
        if b[size] > 0:
            # add to income
            monayyy = monayyy + price
            # and substract
            b[size] = b[size] -1
            # does it disapear if it hits 0 ???? will it stop counting ??? ... 
            #print(b)
            #print(monayyy)
            # fuck no it stays there. i need to add it must be positive i guess 
print(monayyy)

# Collections.namedtuple()
#Can you solve this challenge in 4 lines of code or less?
# no...no i can't... why do you want to hurt me you sadistic thing

from collections import namedtuple
a = int(input())
cate = input().split()
tot_grade = 0

for x in range(a):
    test = namedtuple("test", cate)
    #pt1 = test(input().split()) gets me 3 missing arguments
    # This gets me the 4 values each time
    first, second, third, fourth = input().split()
    # like pt1    
    pt1 = test(first, second, third, fourth)
    # the x here is the field so i want MARKS
    tot_grade += int(pt1.MARKS)

print((tot_grade/a))


#Collections.OrderedDict()
from collections import OrderedDict
from collections import Counter
n = int(input())
ordered_dictionary = {}

for x in range(n):
    value1, value2 = (input().rsplit(sep=" ", maxsplit=1))
    if (ordered_dictionary[value1] == int(value2)) in ordered_dictionary:
            ordered_dictionary[value1] = int(value2)*2
    else:
        ordered_dictionary[value1] = int(value2)

print(ordered_dictionary)

# Collections.deque()

from collections import deque
d = deque()
a = int(input())

for x in range(a):
    instruc = list(input().split())
    if len(instruc) >1 :
        exec("d." + instruc[0]+"(instruc[1])")
    else:
        exec("d."+instruc[0]+"()")

print(*d)

# SECTION: Date and Time

# Calendar Module
import calendar as cal

day, month, year = map(int, input().split(" "))
#freaking american format
print((cal.day_name[cal.weekday(year,day,month)]).upper())

# SECTION: Errors and Exceptions

#Exceptions
n = int(input())

for x in range(n):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
        
# Incorrect Regex 
import re
n = int(input())

for x in range(n):
    test = input()
    try:
        regex = re.compile(test)
        print(True)
    except re.error:
        print(False)


# SECTION: Builtins

# Zipped!
x,n = map(int, input().split(" "))

empty = []
for y in range(n):
    empty.append((map(float, input().split(" "))))

for z in zip(*empty): 
    print(sum(z)/n)
    
#ginortS
string = sorted(input())

lower = []
upper = []
odd = []
even = []

for x in string:
    if x.isalpha():
        if x.islower():
            lower.append(x)
        else:
            upper.append(x)
    else:
        if int(x) % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

test = "".join(lower+upper+odd+even)
print(test)


# SECTION: Functionals

# Map and Lambda Function
cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        fibo = []
    elif n == 1:
        fibo = [0]
    else:
        fibo = [0,1]
        for x in range(2,n):
            new_num = fibo[x-1] + fibo[x-2]
            fibo.append(new_num)

    return fibo

# SECTION: REGEX

# Detect Floating Point Number
import re
n = int(input())

regex_1 = r"[+-.|0-9]*\.[0-9]+$"
regex_2 = r"^[-+]?[0-9]*\.[0-9]+$"

for x in range(n):
    if re.findall(regex_2, input()):
        print(True)
    else:
        print(False)

# Re.split()

regex_pattern = r"\D+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

# Re.findall() & Re.finditer()
import re

regex = r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])"

test = re.findall(regex, input())
print("\n".join(test or ["-1"]))


# Re.start() & Re.end()
s = input()
k = input()

import re

test = list(re.finditer(r"(?={})".format(k), s))


if not test:
    print("(-1, -1)")
else:
    for x in test:
        print("({0}, {1})".format(x.start(),x.end()+len(k)-1))

#Validating phone numbers
import re
n = int(input())
#A valid mobile number is a ten digit number starting with a 7,8  or 9 

regex = r"[789]\d{9}$"

for x in range(n):
    if re.match(regex,input()):   
        print("YES")  
    else:  
        print("NO")

# Validating and Parsing Email Addresses
import re
import email.utils

n = int(input())
regex = r"\[a-zA-a][a-zA-Z|0-9|-|_|\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}"
# I keep getting the - or .
# so i need to make < the first chracter
regex_1 = r"<[a-zA-Z][a-zA-Z|0-9|-|_|\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
# I need to group [a-zA-Z|0-9|-|_|\.]
regex_2 = r"<[a-zA-Z](\w|-|\.|_)+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"

for x in range(n):
    name, address = input().split(" ")
    if re.match(regex_1, address):
        print(name, address)

# Hex Color Code
import re
n = int(input())
regex_1 = r"\S*: .*"
regex_2 = r"#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3}"
regex_test = r"font-size"

empty = []
for x in range(n):
    matches = re.findall(regex_1, input())
    if matches:
        test = re.findall(regex_2, str(matches))
        if test != []:
            empty.append(test)

for i in empty:
    if len(i) == 1:
        print(*i)
    else:
        for y in range(len(i)):
            print(i[y])

#HTML Parser - Part 1
n = int(input())
# ok, we have the skeleton
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ("Start :",tag)
            # How the fuck do I use attrs
        for x in attrs:
            print ("->",x[0],">",x[1])
            
    def handle_endtag(self, tag):
        print ("End   :",tag)
        
    def handle_startendtag(self, tag, attrs):
        print ("Empty :",tag)
        for x in attrs:
            print ("->",x[0],">",x[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for x in range(n)]))


# Detect HTML Tags, Attributes and Attribute Values
n = int(input())
# Well ... i am gonna do like the other
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
#        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        for x in attrs:
            print ("->",x[0],">",x[1])

parser = MyHTMLParser()
parser.feed(" ".join([input() for x in range(n)]))


# SECTION: Closures and Decorators

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f(["+91 "+ num[-10:-5]+ " " +num[-5:] for num in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

# Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        # complete the function
        # operator.itemgetter()
        # return people -> get me the listS 
        # return operator.itemgetter(-1)([x for x in people]) -> return all the elements from the last name
        # I have to use map to " retrieve specific fields from a tuple record:"
        # list should also work
        # YASSS
        # so I want to SORT on that
        the_list = [x for x in people]
        get_last = operator.itemgetter(2)
        #age = map(get_last, the_list)
        # YASSS
        thing = sorted(the_list, key= lambda x: int(x[2]))
        # does not work...because the num is a string
        # operator item is sh#t
        return map(f, thing)

    
    return inner

# SECTION : Numpy

# Arrays
import numpy

def arrays(arr):
    test = numpy.array(arr, float)
    test = numpy.flip(test)
    return test

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Shape and Reshape
import numpy as np

test = np.array(input().split(" "), int)
test = np.reshape(test, (3,3))
print(test)

# Transpose and Flatten
import numpy as np

n,m = map(int, input().split(" "))

empty = []
for x in range(n):
    empty.append(input().split(" "))

arr = np.array(empty, int)

trans_arr = np.transpose(arr)
flat_arr = arr.flatten()

print(trans_arr)
print(flat_arr)

# Concatenate
import numpy as np

n,m,p = map(int, input().split(" "))

empty = []

for x in range(n+m):
    empty.append(input().split(" "))

arr = np.array(empty, int)
print(arr)

#Zeros and Ones
import numpy as np
abc = tuple(map(int, input().split(" ")))

zero = np.zeros(abc, dtype = np.int)

one = np.ones(abc, dtype= np.int)

print(zero)
print(one)

# Eye and Identity
import numpy as np

n,m = map(int, input().split(" "))
matrix = str(np.eye(n, m)).replace("1"," 1").replace("0"," 0")
print(matrix)

#Array Mathematics
import numpy as np
n,m = map(int, input().split(" "))

a = np.array([input().split() for x in range(n)],dtype=int)
b = np.array([input().split() for x in range(n)],dtype=int)

print((a+b))
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

#Floor, Ceil and Rint
# The solution requires some "space". I took the line of code from the solutions. this happens several time  
import numpy as np
# I am not going to fight for a space
np.set_printoptions(sign=' ')

arr = np.array(input().split(), float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

# Sum and Prod
import numpy as np

n,m = map(int,input().split(" "))
arr = np.array([(input().split(" ")) for x in range(n)], int)
print(np.prod(np.sum((arr), axis=0)))

# Min and Max
import numpy as np

n,m = map(int, input().split(" "))
arr = np.array([input().split(" ") for x in range(n)], int)
print(np.max(np.min(arr, axis=1)))

# Mean, Var, and Std
import numpy as np
# Not fighting for a space
np.set_printoptions(legacy='1.13')

n,m = map(int, input().split(" "))
arr = np.array([input().split() for x in range(n)], float)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))

# Dot and Cross
import numpy as np
 
n = int(input())
a = np.array([input().split(" ") for x in range(n)], int)
b = np.array([input().split(" ") for x in range(n)], int)
print(np.matmul(a,b))

# Inner and Outer
import numpy as np

a = np.array(input().split(" "), int)
b = np.array(input().split(" "), int)

print(np.inner(a,b))
print(np.outer(a,b))

# Polynomials
import numpy as np

p = np.array(input().split(" "), float)
x = float(input())

print(np.polyval(p,x))

# Linear Algebra
import numpy as np
# Not fighting Again
np.set_printoptions(legacy='1.13')

n=int(input())
a = np.array([input().split() for x in range(n)], float)
print(np.linalg.det(a))

# SECTION: XML

# XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree
#n = int(input())
#haaa = []
#for x in range(n):
#    haaa.append(input())
#xml = "".join(haaa)
#tree = etree.ElementTree(etree.fromstring(xml))
#root = tree.getroot()

def get_attr_number(node):
    #attributes = []
    #for x in node.iter():
    #    print(x.attrib)

    test = [len(x.attrib) for x in node.iter()]
    return sum(test)
    #return sum(len(child.attrib) for child in node.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

# XML2 - Find the Maximum Depth
# With the assistance of the solutions for the for loop. 

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
        
    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
