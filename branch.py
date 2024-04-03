# Name: Carson Allen
# Prog Purpose: Find the cost of a meal at Branch Barbeque Buffet

import datetime

ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SERVICE_FEE_RATE = .1
SALES_TAX_RATE = .062

num_adult_meals = 0

def main():
    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)?")
        if yesno == "N" or yesno == "n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meals, num_child_meals
    num_adult_meals = int(input("How many adult meals would you like to order? "))
    num_child_meals = int(input("How many child meals would you like to order? "))

def perform_calculations():
    global subtotal, service_fee, sales_tax, total, adult_total, child_total
    adult_total = num_adult_meals * ADULT_MEAL
    child_total = num_child_meals * CHILD_MEAL
    subtotal = adult_total + child_total
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

def display_results():
    currency = '8,.2f'
    date = str(datetime.datetime.now())
    fdate = date[0:16]
    print("------------------------------------------")
    print("********* Branch Barbeque Buffet *********")
    print("------------------------------------------")
    print("Quantity of Adult Meal(s):       " + str(num_adult_meals))
    print("Total price of Adult Meal(s):      $" + format(adult_total, currency))
    print("Quantity of Child Meal(s):       " + str(num_child_meals))
    print("Price of Child Meals(s):           $" + format(child_total, currency))
    print("------------------------------------------")
    print("Subtotal:                          $" + format(subtotal, currency))
    print("Service Fee:                       $" + format(service_fee, currency))
    print("Sales Tax:                         $" + format(sales_tax, currency))
    print("------------------------------------------")
    print("Total:                             $" + format(total, currency))
    print(fdate)

main()
