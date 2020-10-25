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

#



