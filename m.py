
# def my_name():
#     print("my name is Thamer ")

# my_name()


# def my_meal(food , drink):

    
#     print(f"I like to eat {food} and while drinking {drink}")
    
# my_meal("burger" , "pepsi")

def cube(num3):
    num = num3 **3
    return print(num)

def by_three(num3):
    if num3%3 == 0 :
        cube(num3)
    else:
        print(False)

num3 = eval(input("enter a num :"))
by_three(num3)