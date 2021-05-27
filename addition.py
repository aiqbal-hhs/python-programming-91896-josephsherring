i=0

def counting():
    while i(1, 20):
        print(i)
        i+1
    
def greeting():
    firstname = str(input("What is your first name? "))
    lastname = str(input("what is your last name? "))
    print("Hello {} {}! ".format(firstname, lastname))

def addition():
    question_one = int(input("give me a whole number: "))
    question_two = int(input("give me another whole number: "))
    print("If you add these togeather you get:", question_one + question_two)

def rectanglearea():
    width = int(input("give me the width of the rectangle: "))
    length = int(input("give me the length of the rectangle: "))
    print("If you times these togeather you get the area of the rectangle which is:", width * length)

greeting()
addition()
rectanglearea()
