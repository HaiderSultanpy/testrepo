# fruit_basket= 'manoes'
# print(fruit_basket)
# fruit_basket= input("which is your fav fruit?")
# print (fruit_basket)

# name= input("what is your name? ")
# greetings= "Hello"
# print(greetings, name)

name= input("what is your name?" )
age= int(input ("how old are you? "))
greetings= "Hello"
if age<5:
    print(greetings, name, "you're too young for school")
elif age==5:
    print (greetings, name,"you're eligible")
else:
    print (greetings, name,"you're too old")