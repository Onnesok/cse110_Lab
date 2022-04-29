###################### Task 1  ###############################
################### buble sort  ##########################
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

index = len(my_list) - 1

for i in range(len(my_list)):
    for j in range(len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            temp = my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp

print(my_list)

###################### Task 2 ###################################
#################### selection sort ###########################

my_list= [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

for i in range(len(my_list)):
    temp = my_list[i]
    for j in range(i+1, len(my_list)):
        if my_list[i] > my_list[j]:
            swap = my_list[i]
            my_list[i] = my_list[j]    
            my_list[j] = swap

print(my_list)


#########################  Task 3 ###############################
######################## using selection sort  ##################

my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

for i in range(len(my_list)):
    temp = my_list[i]
    for j in range(i+1, len(my_list)):
        if my_list[i] < my_list[j]:
            swap = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = swap
print(my_list)

#################### Task 4  ##################################
###################################################

def odd_descending(my_list):
    for i in range(len(my_list)):
        temp = my_list[i]
        for j in range(i+1, len(my_list)):
            if my_list[i] < my_list[j]:
                swap = my_list[i] 
                my_list[i] = my_list[j]
                my_list[j] = swap
    
    return my_list

def even_ascending(my_list):
    for i in range(len(my_list)):                                               
        temp = my_list[i]
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                swap = my_list[i]
                my_list[i] = my_list[j]     
                my_list[j] = swap
        
    return my_list


sitting_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80,5]

even = []
odd = []
final = []
for i in range(len(sitting_list)):
    if i %2 == 0:
        even.append(sitting_list[i])
    else:
        odd.append(sitting_list[i])

even_f = even_ascending(even).copy()
odd_f = odd_descending(odd).copy()

if len(even_f) == len(odd_f):
    for k in range(len(even_f)):
        final.append(even_f[k])
        final.append(odd_f[k])
elif len(even_f) > len(odd_f):
    for k in range(len(odd)):
        final.append(even_f[k])
        final.append(odd_f[k])
    final.append(even_f[k+1])

print(final)

######################################  Task 5 #######################

lst = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]

user = input("please enter course code: ")

temp = ["Alan", "Turing", "Elon", "Musk"]

if user == "CSE110":
    for i in range(len(lst)):
        temp = lst[i][1]
        for j in range(i+1, len(lst)):
            if lst[i][1] < lst[j][1]:
                swap = lst[i]
                lst[i] = lst[j]
                lst[j] = swap


if user == "PHY111":
    for i in range(len(lst)):
        temp = lst[i][2]
        for j in range(i+1, len(lst)):
            if lst[i][2] < lst[j][2]:
                swap = lst[i]
                lst[i] = lst[j]
                lst[j] = swap

if user == "MAT110":
    for i in range(len(lst)):
        temp = lst[i][3]
        for j in range(i+1, len(lst)):
            if lst[i][3] < lst[j][3]:
                swap = lst[i]
                lst[i] = lst[j]
                lst[j] = swap

for k in range(len(lst)):
    print(lst[k][0])


#############################  Task 6  #######################

my_list = [4, 2, 3, 1, 6, 5]
count = 0
ls = my_list.copy()

for i in range(len(my_list)):
    temp = my_list[i]
    for j in range(i+1, len(my_list)):
        if my_list[i] > my_list[j]:
            swap = my_list[i]
            my_list[i] = my_list[j]     
            my_list[j] = swap
    if ls[i] != my_list[i]:
        count += 1
print(count)

######################## Task 7 #############################

ls1 = [int(user) for user in input("please enter list items: ").split(",")]
ls2 = [int(user) for user in input("please enter list items: ").split(",")]

ls3 = ls1 + ls2

for i in range(len(ls3)):
    temp = ls3[i]
    for j in range(i+1, len(ls3)):
        if ls3[i] > ls3[j]:
            swap = ls3[i]
            ls3[i] = ls3[j] 
            ls3[j] = swap

mid = len(ls3) // 2
res = (ls3[mid] + ls3[-mid-1]) / 2
print("Sorted list = ", ls3)
print("Median = ", res) 

#######################  Task 8  ####################################
user = input("please enter an input: ")[1:-1].split(",")
min_1 = 0
min_2 = 1
min_sum = int(user[0]) + int(user[1])

for i in range(len(user)-1):
    for j in range(i+1, len(user)):
        sum = int(user[i]) + int(user[j])
        if abs(min_sum) > abs(sum):
            min_sum = sum
            min_1 = i
            min_2 = j

print(f"Two pairs which have the smallest sum = {user[min_1]} and {user[min_2]}")

####################### Task 9 ############################
import math

points = [(1,7), (4,5), (-1,7), (-2,0), (1,1), (5,-1)]

res = 9999999999999999
pair = 0

for i in range(len(points)):
    temp = points[i]
    cal = math.sqrt(((temp[0]-0)**2)+((temp[1]-0)**2))
    if cal < res:
        res = cal
        pair = temp

print(f"Minimum distance = {res}")
print(f"Here the closest point is {pair} which has a distance of {res} from the origin.")