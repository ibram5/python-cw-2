my_name = input("enter your name:")
my_age = input("enter your age:") 
print(f"My name is {my_name} and I am {my_age} years old")  


first_number = float(input("enter the first number:"))
secound_number = float(input("enter the secound number:"))
operation = input("enter an operation (/,*,-,+):")

if operation == "+" : 
    print(first_number + secound_number)
elif operation == "-":
    print(first_number - secound_number)
elif operation == "*":
    print(first_number * secound_number)
elif operation == "/":
    print(first_number / secound_number)
else : 
    print("the operation is not valid")
    
    
bus_capacity = 40
people_inbus = int(input("enter the number of people in bus :"))
people_want_to_enter = int(input("enter the number of people how want to enter the bus ")) 
empty_seats = bus_capacity - people_inbus
    
if empty_seats > people_want_to_enter : 
        print("you can enter the bus")
elif empty_seats <= people_want_to_enter :
        print("the bus is full")
    
    
    