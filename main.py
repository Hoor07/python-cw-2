myname = input('what is your name')


myage = input('how old are you')

print(f"My name is{myname} and i am {myage} years old")


frist_number=int(input(' choose a number'))
secound_number=int(input('choose a number'))
operation=input("what is your operation")
if operation == "+" :
    print(frist_number + secound_number)   
elif operation == "-" :
    print(frist_number - secound_number)   
elif operation == "*" :
    print(frist_number * secound_number)     
elif operation == "/" :
    print(frist_number / secound_number) 
else:
    print ('the operation is not vaild')
   
   
   
bus_capacity=4
peopleinside = int(input("how many people in the bus"))
peoplewateing= int(input("how many people do want to go in the bus") )
empty_seats= bus_capacity- peopleinside
if empty_seats>=peoplewateing:
    print ('getin')
else: 
    print ("sorry no seats") 