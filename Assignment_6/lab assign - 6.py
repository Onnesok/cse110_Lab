################## Task 1  #################################
def even_checker(user):
    if user % 2 == 0:
        print("Even!!")
    else:
        print("Odd!!")

user = int(input("please enter an input: "))

even_checker(user)


################### Task 2  ################################
def fibonacci(user):
    num1 = 0
    num2 = 1
    rs = 0
    print(num1, num2, end = " ")
    while rs <= user:
        rs = num1 + num2
        num1 = num2
        num2 = rs
        if rs <= user:
            print(rs, end = " ")
        else:
            break


user = int(input("please enter an input: "))
fibonacci(user)


####################### Task 3 #######################

def foo_moo(user):
    if user%2 == 0 and user%3 == 0:
        return "FooMoo"
    elif user%2 == 0:
        return "Foo"
    elif user%3 == 0:
        return "Moo"
    else:
        return "Boo"

user = int(input("please enter an input: "))

print(foo_moo(user))

###################### Task 4  ########################

def letter(user):
    upper = 0
    lower = 0
    for i in range(len(user)):
        if ord(user[i]) >= 65 and ord(user[i]) <= 90:
            upper  += 1
        elif ord(user[i]) >= 97 and ord(user[i]) <= 122:
            lower += 1
    
    print(f"No. of Uppercase characters : {upper}")
    print(f"No. of Lowercase characters : {lower}")

user = input("please enter an input: ")
letter(user)

##################### Task 5  ##########################

def calculate_tax(age, salary, position):
    if age < 18 or salary < 10000 or position.lower() == "president":
        return 0
    elif age >= 18 and salary >= 10000 and salary <= 20000 and position.lower() != "PRESIDENT":
        return (salary * (5/100))
    elif age >= 18 and salary > 20000 and position.lower() != "president":
        return (salary * (10/100))
age = int(input("please enter age data: "))
salary = int(input("please enter your salary data: "))
position = input("please enter your job position: ")

print(calculate_tax(age, salary, position))


###################  Task 6 ###########################

def time(user):
    year = user // 365
    month = (user - year*365) // 30
    days = (user - year*365 - month*30)
    print(f"{year} years, {month} months and {days} days")

user = int(input("please enter number of days: "))
time(user)

################## Task 7  ###########################

def show_palindrome(user):
    st = ""
    i = 1
    while i < user+1:
        st = st + str(i)
        i = i+1
    i = i-2
    while i != 0:
        st = st + str(i)
        i = i-1
    return st

user = int(input("please enter an input: "))
print(show_palindrome(user))

################# Task 8  ###########################

def show_palindrome(user):
    st = ""
    i = 1
    while i < user+1:
        st = st + str(i) + " "
        i = i+1
    i = i-2
    while i != 0:
        st = st + str(i) + " "
        i = i-1
    return st

def show_palindromic_triangle(n=5):
    k = n-1

    for i in range(n):
        print(" "*2*k, end="")
        k = k-1
        print(show_palindrome(i+1))
        #print()

n = int(input("please enter a number:"))
show_palindromic_triangle(n)

#################### Task 9  ############################
import math

def area_circumference_generator(radius):
    area = math.pi*radius**2
    circumference = 2*math.pi*radius
    tp = (area, circumference)
    return tp

user = float(input("please enter a radius: "))
area, circumference = area_circumference_generator(user)
print(area_circumference_generator(user))
print(f"Area of the circle is {area} and circumference is {circumference}")

#####################  Task 10  ##########################

def make_square(tp):
    t1,t2 = tp
    d1 = {}
    for i in range(t1, t2+1):
        d1[i] = i**2
    print(d1)

make_square((5,9))

####################  Task 11  #############################

def rem_duplicate(tp):
    ls2 = []
    ls1 = list(tp)
    for i in range(len(ls1)):
        if ls1[i] not in ls2:
            ls2.append(ls1[i])
    
    print(tuple(ls2))

rem_duplicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))


######################  Task 12  ################################

def fn(lst):
    ls1 = []
    count = 0
    for i in range(len(lst)):
        if ls1.count(lst[i]) < 2 :
            ls1.append(lst[i])
        else:
            count += 1

    print("Removed:",count)
    return ls1

print(fn([10, 10, 15, 15, 20]))


#####################  Task 13   #################################
def fn(sign, n1,n2):
    if sign == "*":
        return(n1*n2)
    elif sign == "/":
        return (n1/n2)
    elif sign == "+":
        return (n1+n2)
    elif sign == "-":
        return (n1-n2)


sign = input("please enter a sign: ")
n1 = float(input("please enter 1st number: "))
n2 = float(input("please enter 2nd number: "))

print(fn(sign, n1, n2))


#####################  Task 14   #################################
def fn(sentence, position):
    s1 = sentence[0]
    rm_s = ""
    for i in range(1, len(sentence)):
        if i % position != 0:
            s1 = s1 + sentence[i]
        elif i % position == 0:
            rm_s = rm_s + sentence[i]
    final = s1 + rm_s
    return final


sentence = input("please enter a sentence: ")
position = int(input("please enter a position: "))
print(fn(sentence, position))
#####################  Task 15   #################################
def fn(ls1, location = "Dhanmondi"):
    d1 = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    cost = 0
    #for key, value in d1.items():
    for i in range(len(ls1)):
        cost += d1.get(ls1[i])
        #break
    
    if location == "Dhanmondi":
        cost = cost + 30
    else:
        cost = cost + 70
    return cost
    


ls1 = []
ls1 = [user for user in input("please enter list items: ").split()]
location = "Mohakhali"
print(fn(ls1, location))





################  20  #############

i = 2
j = 0
k = 17
test = "-->dog"
while i < 7:
    k-=1
    j = k
    while j > 12:
        if (j % 2 == 0):
            test += "<--"
            test = test + str(i) + str(j // 2)
        else:
            test += "-->"
            test = test + str(i // 2) + str(j)
        print(test)
        j-=1
        i+=1

#################### 21 ##########################

test = ""
i = 5
j = 0
k = 15
while (i< 10):
    k-=1
    j = k
    while (j > 10 ):
        if j % 2 == 0:
            test = "<--"
            test = test + str(i) + '3' + "-->" + str(j // 3)
        else:
            test = "-->"
            test = "-->" + str((i // 3)) + test + str(j)
        print(test)
        j -=1
    i+=1


#############  22  ################

i = 10
while(i >= -20):
    if(i < 0):
        test = " != "
        test = str(i//2) + test + str(int(i/2))
    else:
        test = " == "
        test = str(i//2) + test + str(int(i/2))
    print(test)
    i -= 5
