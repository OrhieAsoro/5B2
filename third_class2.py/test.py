# def slug(word):
#     return word.replace(" ", "-").lower()

#print(slug('How do you cook'))

# def char(string1, string2):
#     a = string1[:2]
#     b = string2[-2:]
#     return a+b

# print(char('Adaobi', 'United'))
# a =lambda x : x + 15
# print(a(15))

# tim = lambda a,b : a*b
# print(tim(20,30))



# converts = lambda string : string.swapcase()

# print(converts("I AM A BOY"))

# file_name = input("File name\n")
# print(file_name.split(".")[-1])

# v = [12, 30, 10, 13, 23]
# trippled = list(map(lambda x : 3*x, v))
# squared = list(map(lambda x : x**2, v))

# print(trippled)
# print(squared)
# a=[]
# print(type(a))
#be = [6,7,9,0,2,1,8]
# he = [3,4,6,1,8,0]
# print(be[3])

# print(be[2:6:2])
# be[4]= 20
# print(be)
#


# v= [2,3,4,2,[2,3,4,5, [4,52,2],5],24]
# a = v[4][4][1]
# b = v[5]
# print(a+b)



# D= [2,30,67,62,98,41,5]
# D.sort()
# print(D[1])
# print(D[-2])
# print(D[:3])
# print(D[-3:])

#def largest(arr:list, k:int):
#     """This function returns the highest k value in an array: arr"""
#     arr.sort(reverse=True)
#     return arr[:k]


# def smallest(arr:list, k:int):
#     """This function returns the lowest k value in an array: arr"""
#     arr.sort()
#     return arr[:k]
    
# print(largest([2,30,67,62,98,41,5],2))
# print(smallest([2,30,67,62,98,41,5],2))

# t = ['A','b','z','F','r']
# b= list(filter(lambda x : x.isupper(),t))
# print(b)


# user =input('Write number\n').split(",")
# mapped=map(int,user)
# odd_numbers=filter(lambda x :x % 2==1, mapped)
# print(list(odd_numbers))
# a =[1,2,3]
# b =[1,2,3]
# print(a==b)
# print(a is b)



# a=[4,7,9]
# b=a
# c=a.copy()
# print(b is a)
# print(c is a)

#t=[20,23,76,90,97,764,322]
# def middle(t):
#     return t[1:-1]
# print(middle(t))

# def median(t):
#     t.sort()
#     mid_point = len(t)//2
#     if len(t)%2==0:
#         return (t[mid_point] + t[mid_point-1])/2

#     return t[mid_point]


# t=[20,23,76,90,94, 97,764,322]
# print(median(t))
# John = "Present"
# if John == "Present":
#     print("Present")
# else:
#     print("Absent")
#Orhie= 25
# if Orhie < 18:
#     print("Underage")
# elif Orhie == 18:
#     print("Correct age")
# elif Orhie > 18:
#     print("Overage")

# if Orhie <=18:
#     if Orhie < 18:
#         print("Under age")
#     else:
#         print("Correct age")
# else:
#     print("Overage")

# score =int(input("What is your exam score\n"))

# if score <= 39:
#     print("F")
# elif score <= 49:
#     print("E")
# elif score <= 59:
#     print("D")
# elif score <= 69:
#     print("C")
# elif score <= 79:
#     print("B")
# elif score <= 100:
#     if score <= 90:
#         print("A-")
#     else:
#         print("A+")
# else:
#     print("Missing Results")
# import random
# a = [3,2,5,6,8,7]

# print(f"Select any number from {a}. \nWe hope it doesn't end in tears.")
# com_choice = random.choice(a)
# random.shuffle(a)
# print("Guess the number:")
# user_choice = int(input(">"))

# if user_choice in a:
#     if user_choice == com_choice:
#         print("All power belongs to you, comrade.")
#     else:
#             print("Arrhh,comrade. Be like you go try again")
# else:
#         print("Comrade, nor be so!")

text = "I am a very good boy"
sub_text = input("Enter text to search for:\n").lower()

lowercase_text = text.lower()
found = lowercase_text.find(sub_text)
count = lowercase_text.count(sub_text)

if found != -1:
    print(f"{count} result(s) found!")
    new_text = text.replace(sub_text,sub_text.upper())
    print(new_text)
else:
    print(f"{count} result(s) found!")