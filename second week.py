
#1
name = "ahmed"  
age = 21       
country = "Egy"  
x = "Hello '" + name + ", how You Doing \\ \"\"\" Your Age Is \"" + str(age) + "\"\" + And Your Country Is: " + country
print(x)
#2
y = "Hello '" + name + ", how You Doing \\\n \"\"\" Your Age Is \"" + str(age) + "\"\"\n + And Your Country Is: " + country
print(y)
#3
nam='elzero'

print('first letter '+nam[1])
print('second letter '+nam[2])
print('third letter '+nam[5])
#4
print('first letter '+nam[1:4])
print('second letter '+nam[0]+nam[2]+name[4])
print('third letter '+nam[4]+nam[2]+nam[0])
#5
xx='#@elzero#@'
print(xx.strip('#@'))
 
 #6
num1 = 15
num2 = 130
num3 = 950
num4 = 1500
print( num1)
print(num2)
print(num3)
print(num4)
#7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,'@'))
print(name_two.rjust(20,'@'))
#8
namex = "OSamA"
namey = "osaMA"
print(namex.swapcase())
print(namey.swapcase())