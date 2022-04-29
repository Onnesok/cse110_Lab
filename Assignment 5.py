###################### Task 1 ############################

a_tuple = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821), 75717,
[1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))

print(a_tuple[3][3])


###################### Task 2    ######################

tuple_g = (10, 20, 24, 25, 26, 35, 70)
tuple1 = (tuple_g[2:-2])
print(tuple1)


#####################  Task 3 #############################

book_info = (
("Best Mystery & Thriller","The Silent Patient",68,821),
("Best Horror","The Institute",75,717),
("Best History & Biography","The five",31,783 ),
("Best Fiction","The Testaments",98,291)
)

print("Size of the tuple is: ", len(book_info))
for i in book_info:
    print(i)

################## Task 4 #######################

book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
)

for tuple1 in book_info:
    category, book, vote = tuple1
    print(f"{book} won the {category} category with {vote} votes ")

##################### Task 5 #########################

given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
count = 0
tp = float(input("please enter a number: "))

for i in range(len(given_tuple)):
    if tp == given_tuple[i]:
        count = count + 1
print(int(tp), "appears", count, "times in the tuple")

####################### Task 6 ########################

given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

list2 = []
list1 = list(given_tuple)
for i in range(len(given_tuple)-1, -1, -1):
    list2.append(list1[i])
print(tuple(list2))

#################### Task 7 #####################

d1 = {'Harry':15, 'Draco':8, 'Nevil':19}
d2 = {'Ginie':18, 'Luna': 14}
mark = {**d1, **d2}
print(mark)


  Another way
d1 = {'Harry':15, 'Draco':8, 'Nevil':19}
d2 = {'Ginie':18, 'Luna': 14}
mark = {}
mark.update(d1)
mark.update(d2)
print(mark)


################ Task 8  #######################

def f1(d_st):
    cnt = 0
    for i in d_st:
        cnt = cnt+1
    return cnt

d_st = input("please enter a dictionary: ")[1:-1].split(",")
temp = []
c = ""
str1 = ""
count = 0
rs = 0
for i in range(f1(d_st)):
    c=d_st[i]
    for j in range(f1(d_st[i])):
        if c[j] == ":":
            str1 = c[j+1:f1(c)]
            p = str1.strip()
            rs = rs + int(p)
            count = count + 1
print("Average is:", int(rs/count))

################### Task 9 ########################

exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}

c = exam_marks.copy()
user = int(input("please enter a number: "))
d1 = {}

for i in exam_marks:
    p = int(exam_marks[i])
    if p < user:
        del c[i]
    
print(c)

################ Task 10 ###########################

d1 ={'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}

mx = -99999

for i in d1:
    if mx < d1[i]:
        mx = d1[i]
        rs = "'"+i+"'"
print("The highest selling book genre is", str(rs), "and the number of books sold are", mx)

############### Task 11 ############################

user = input("please enter a input: ")
user = user.lower()
d1 = {}
for i in range(len(user)):
    if user[i] != " ":
        temp = user[i]
    count = 0
    for j in range(len(user)):
        if temp == user[j]:
            count = count + 1
    d1[temp] = count
print(d1)

#################### Task 12   #########################
dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count = 0
for key, value in dict_1.items():
    for items in value:
        count = count + 1
print(count)
##################### Task 13 ##########################

list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]

d1 = {}
cnt = 0

for i in range(len(list_1)):
    lst = []
    temp = list_1[i][0]
    for j in range(len(list_1)):
        if temp == list_1[j][0]:
            if list_1[j][1] not in lst:
                lst.append(list_1[j][1])
    
    d1[temp] = lst
print(d1)

        
        