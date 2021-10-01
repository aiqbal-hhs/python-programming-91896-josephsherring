import sys
#Allows the program to know that these all mean the same thing
yeslist = ["yea", "yes", "y", "yeah", "ok", "yep"]
nolist = ["no", "n"]
#Sets the price and pizza orders to 0
price = 0
price_total = 0
p_max = 0
success = False
#List of all the pizzas and toppings to call back to later
pizzalist = ("Cheese", "Cheesy Garlic", "Pepperoni", "Hawaiian", "Ham and Cheese", "Bacon", "Classic Veggie", "Margherita", "Meat lovers", "Loaded Hawaiian", "Loaded Pepperoni", "Supreme")
toppingslist =  ("With Jalapenos", "With Olives", "With Pineapples", "With Mushrooms", "With Extra Cheese", "With Ham")
#Empty list which is added to create the order
order = []
#list which will store different information for the order such as address and name
details = []
name_details = []
delivery_details = []

#Defines get_int so when inserted into the code it stops value errors from happening so the program runs smoother and is less overall lines
def get_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
            break
        #When a value error is triggered it will return the question again
        except ValueError:
            print("Please make sure you enter an integer value in your answer.\n============================================================")
    return answer

#Defines a function that will reduce the words needed when a yes or no question is answered, removing unnecassary elif and else statements
def get_yesno(prompt):
    while True:
        answer = str(input(prompt))
        #Returns question if the user answers something not inside the yeslist or nolist
        if answer not in yeslist and answer not in nolist:
            print("Please make sure you enter Y/N.\n")
            continue
        else:
            break
    return answer

#defines what start means
def start():
    #asks the user if they would like to run the program
    run = str(get_yesno("Would you like to run the program?[Y/N]\n>>> "))
    #creates a loop so that as long as the user answers incorrectly to the question they will be asked again til a correct answer is provided
    while True:
        #If the user answers one of the answers in the list I created with accetable 'no' answers it will run this
        if run.lower() in nolist:
            print("Closing program")
            sys.exit()
        #If the user answers with an acceptable 'yes answer from the yeslist then the loop will be stop
        else:
            break



#Defines the delivery function which asks the user about the method of picking up the pizza they want
def delivery():
    global price
    global order_type
    #Asks the user if they want pickup or delivery then stores their answer in order_type
    order_type = str(get_int("\nWould you like to recieve your order via Pick up [1] or delivery [2]\n>>> "))
    #confirms the address is correct with a while loop so when it is incorrect the loop will repeat
    while True:
        if order_type == "2":
            print("\n\nOption 2 - delivery.")
            #asks the user what their address is if they chose delivery then confirms it is correct
            address = str(input("\nWhat is the customers address? \n>>> "))
            correct = str(get_yesno("\nIs this the correct address?[Y/N]]\n[{}]\n>>> ".format(address)))
            if correct.lower() in yeslist:
                delivery_details.append("Address: " + address)
                break
            else:
                continue
        elif order_type == "1":
            print("Option 1 - pick up.\n")
            break
        else:
            print("That is not a valid answer! please pick [1] for pick up or [2] for delivery below")
            order_type = str(get_int(">>> "))
            continue

#Defines the function 'name' which stores the users name and makes sure that it is correct using a loop
def name():
    while True:
        #asks the user their name and makes sure the name entered was correct. correct uses get_yesno function to remove unneccasry elif and else statements
        name = str(input("\nWhat is the customers name?\n>>> "))
        correct = str(get_yesno("\nIs this the correct Name?[Y/N]\n[{}]\n>>> ".format(name)))
        #if their name is correct it will be added to name details list to be recalled at the end as the receipt is printed
        if correct.lower() in yeslist:
            name_details.append("Name: ")
            name_details.append(name.title())
            name_details.append(".")
            break
        else:
            continue

#Defines the function 'phone' which stores the users name and makes sure that it is correct using a loop
def phone():
    while True:
        #asks the user their phone number and uses get_int and get_yesno to reduce the lines and make it more streamlined
        phone_num = str(get_int("\nWhat is the customers phone number?\n>>> "))
        correct = str(get_yesno("\nIs this the correct Phone number?[Y/N]\n[{}]\n>>> ".format(phone_num)))
        if correct.lower() in yeslist:
            details.append("Phone number:")
            details.append(phone_num.title())
            break
        else:
            continue

        
#Defines the p_function function which handles the ordering of the pizzas
def p_function():
    global p_max
    global p_amount
    global price
    global p_order
    global success
    #Sets success to False so that the loop on line 138 can work
    success = False
    #shows the user the different options for pizzas and the costs
    print("""\nClassic pizza options: Cost - $8.50 |      Gourmet pizza options: Cost - $13.50
[1] Cheese                           |    [8] Margherita
[2] Cheesy Garlic                    |    [9] Meat Lovers
[3] Pepperoni                        |    [10] Loaded Hawaiian
[4] Hawaiian                         |    [11] Loaded pepperoni
[5] Ham and Cheese                   |    [12] Supreme
[6] Bacon                            |
[7] Classic Veggie                   |
\n""")
    #makes sure that the order is between 1 and 12 so that the code does not break
    while True:
        #asks the user what pizza they want
        p_order = int(get_int("Please select the corresponding number to the pizza you want\n>>>"))
        if p_order <1 or p_order >12:
            print("Please make sure you enter a number between 1 and 12\n")
            continue
        else:
            break
    p_amount = int(get_int("How many {} pizzas do you want [max 5]?\n>>>".format(pizzalist[p_order - 1])))
    #sets up a loop to only run while success is False and while the statements are True
    while True and not success:
        #Stops p_amount if more than 5 or less than 1
        if p_amount > 5 or p_amount <1:
            print("You can only have 5 pizzas sorry!")
            p_amount = int(get_int("How many of this pizza do you want? You currently have room for {} more pizzas in your order \n>>>".format(5 - p_max)))
            continue
        else:
            p_max += p_amount
            #stops p_amount from being added to the max number of pizzas in the order
            while True:
                if p_max >5:
                    print("You cannot have that many pizzas sorry. Max is 5.")
                    p_max -= p_amount
                    p_amount = int(get_int("How many of this pizza do you want?\n>>>"))
                    p_max +=p_amount
                    continue
                else:
                    #displays the pizzas the user has picked and adds the prices to the total price
                    print("You have added {} {} pizzas ".format(p_amount, pizzalist[p_order - 1]))
                    if p_order >= 1 and p_order <= 7:
                        price += 8.50 * p_amount
                    else:
                        price += 13.50 * p_amount
                    #inserts the toppings function so that the user can  pick toppings if they want
                    toppings()
                    break
        
    
#defines a function in which toppings can be added to the order if needed
def toppings():
    global price
    global price_total
    global success
    #sets success to false to prevent an infinite loop in the p_function function
    success = False
    #asks if the user wants extra toppings and uses get_yesno to reduce lines and to stop errors
    p_topping = str(get_yesno("Would you like extra toppings for this pizza?[Y/N]\n>>> "))
    if p_topping.lower() in yeslist:
        print("""Extra toppings are 50 cents and the choices are below.
[1] Jalapenos                        |      [4] Mushroom
[2] Olives                           |      [5] Extra Cheese
[3] Pineapples                       |      [6] Ham
\n""")
        topping_choice = int(get_int("Please enter the corresponding number next to the topping you want\n>>> "))
        #stops the user from entering a number that isnt in the range of 1 to 6 as there are only 6 toppings
        while True:
            if topping_choice >=1 and topping_choice <= 6:
                price += 0.5*p_amount
                break
            else:
                print("We do not have a topping associated with that number, please enter a number between 1 and 6")
                topping_choice = int(get_int("Please enter the corresponding number to the topping you want\n>>>"))
                continue
    elif p_topping.lower() in nolist:
        print("Ok!")
    #adds to the users total order and displays it
    order.append(p_amount)
    order.append(pizzalist[p_order - 1])
    if p_topping.lower() in yeslist:
        order.append(toppingslist[topping_choice - 1])
    else:
        order.append("with no toppings")
    order.append("$")
    order.append(price)
    #calculates total price
    price_total += price
    price = 0
    order.append(",")
    #prints the current order in a simple format
    print(*order, sep= " ")
    success = True
    
#defines a function that handles if the user wants to add more pizzas
def pizza_order():
    global p_max
    global topping_choice
    global p_topping
    global p_order
    p_max = 0
    global p_amount
    global price
    #inserts the p_function function to give the user the option to begin ordering pizzas
    p_function()
    #checks that the pizza is at max limit so it ends the order
    while True:
        if p_max == 5:
            print("You have reached the limit for pizzas (max 5).")
            #adds the finalise function so the program can end when the user has exactly 5 pizzas
            finalise()
            break
        else:
            #asks the user if they want any more pizzas and uses get_yesno to shorten the code and to validate that the answer is y/n
            if p_amount < 5:
                p_cont = str(get_yesno("Would you like to order another pizza?[Y/N]\n>>> "))
                if p_cont in yeslist:
                    p_function()
                    continue
                else:
                    finalise()
                    break
            else:
                finalise()
                break

#defines the finalise function which is used once the user has reached max amount of pizzas or would like to finish their order
def finalise():
    #tells the user they have finished their order and asks if they would like to procceed with the order or end it without finishing the order so they can cancel if the person ordering no longer wants that order
    print("You have reached the end of your order!\n")
    cancel = str(input("Would you like to finalise the order[F] or cancel[C]? (cancelling will bring you back to the start of the program)\n"))
    while True:
        #makes sure that the user is entering one of the acceptable answers and does the intended input if the correct input is added and reasks the question if an incorrect input is entered
        if cancel.lower() == "f":
            print("Thank you for using this program, a receipt will be printed below.\n\n")
            break
        elif cancel.lower() == "c":
            print("Your order has been cancelled.")
            #asks the user if they would like to restart the program after cancellation or just end the program entirely
            restart()
        else:
            print("Please enter F to finalise the order or C to cancel the order.")
            cancel = str(input(">>>"))
            continue


#defines the function that will print the users receipt if they decide to finalise their order
def receipt():
    global order_type
    global price_total
    #formats the receipt and prints the users details from the lists that had the information added earlier 
    print("Thank you for shopping at Henderson Pizza palace.")
    print(*name_details, sep= "")
    print(*order, sep= " ")
    #adds additional information depending on if the user got their pizza to pick up or deliver
    if order_type == "2":
        #adds the extra cost and displays relevant info in the final receipt
        print("Delivery cost: $3")
        print(*details, sep= " ")
        print(*delivery_details, sep= " ")
        price_total += 3
    else:
        print("Pickup: no extra cost")
    #tells the user what the total cost of the order with all prices added together in an understandable simple format
    print("Total order cost is ${}".format(price_total))

#defines the restart function, which allows the user to restart the program from the beggining or end it
def restart():
    global price
    global order
    global success
    #asks the user if they would like to finish the program then checks their answer is a yes or no answer
    run = get_yesno("\n\nWould you like to restart the program?[Y/N]\n>>> ")
    while True:
        if run.lower() in nolist:
            print("Closing program")
            sys.exit()
        #because of get_yesno only nolist is required for the program to ensure a Y/N answer was given as an invalid answer would have already been stopped by the get_yesno function
        else:
            break
    #resets all of the lists and data from the user
    price = 0
    order.clear()
    name_details.clear()
    details.clear()
    delivery_details.clear()
    success = False
    #runs every function so that the code starts again from the beggining
    delivery()
    name()  
    phone()
    pizza_order()
    receipt()
    restart()

#runs the start function so the user can begin the program
start()
#runs the delivery function so the user is asked the delivery questions
delivery()
#runs the name function so that the user can store the customers name
name()
#runs the phone function which allows the user to input the customers phone into the program to be stored
phone()
#runs the pizza ordering function so that the user can enter the customers order
pizza_order()
#runs the receipt function so that the user has access to the obtained information and so that it can be printed for the customer
receipt()
#runs the restart function so that the program will be able to restart after all other functions are run, allowing the user to restart the program or end it
restart()
