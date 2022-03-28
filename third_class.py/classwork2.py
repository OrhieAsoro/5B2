# arr = [1,2,3,4,5,6]
# avr=(sum(arr)/len(arr))
# print(avr)

# range =(max(arr)-min(arr))
# print(range)

# user =input('Write number\n')
# a= user.split(",")
 
# mapped=list(map(int,a))
# print(mapped)





# age=int(input("Age\n>"))
# current_year=int(input("Current_year\n>"))
# year_born = current_year - age
# print(f"Your year of birth is {year_born}")
from math import sqrt

user =input('Write number\n')
a= user.split(",")
mapped=list(map(int,a))

average =sum(mapped)/len(mapped)
range_ =max(mapped)-min(mapped)

x_mean = map(lambda x : (x-average)**2, mapped)
std = sqrt(sum(x_mean)/len(mapped))
variance =(std**2)

print(f"Mean: {average}")
print(f"Range: {range_}")
print(f"Standard Deviation: {std}")
print(f"Variance: {variance}")
