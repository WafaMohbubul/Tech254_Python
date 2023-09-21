#Functions
#making a functions
def print_something():
    print("Hi")

print_something()

#asign arguments to the function
def print_something2(print_string):
     print(print_string)

print_something2("We can pass anything!")

def greeting(name):
    print(f"Hello, my name is {name}")

greeting("Wafa")

#return statement
def addition(int1, int2):
    return int1 + int2

print(addition(2,2))

#default arguments
def addition2(int1=2, int2=4):
    return int1 + int2

print(addition2())

#multiple arguements
#star can be used for multiple things, In this context - its a wild card. Its up to you what this means.
#by putting star infront, it can be as many arguments as we like. And it can be different arguement types e.g. string, tuple
def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)
    print(type(multiargs))

multi_args(1,2,3,4,5,6)
#funciton above creates a function with one arguement that allows mnay to be inputted when called
# and then loops through all the arguments and prints every argument that has been inputted when called

