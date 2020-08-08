# Question1
result = []
result = [i  for i in range(2000,3200) if i%7 == 0 and i%5 != 0]
print("result", result, len(result))


#question 2

print("enter name")
name = input("enter full name :")
print("name",name)
for i in range(len(name)-1,-1,-1):
	print(name[i],  end="")
print()

#OR
'''
print("enter name")
name = input("enter full name :")
print("name",name)
first_name = name.split(" ")[0]
last_name = name.split(" ")[1]
for i in range(len(first_name)-1,-1,-1):
	print(first_name[i],  end="")
#print(" ")
for i in range(len(last_name)-1,-1,-1):
	print(last_name[i],  end="")
print()
'''
#question 3
dia = 12
pie = 22/7
vol_sphere = 4/3 * pie * (dia/2)**3
print("volume of sphere is : ", vol_sphere)