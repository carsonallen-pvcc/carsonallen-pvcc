# Name: Carson Allen, Albert Chen
# Prog Purpose: Palermo Pizza
import datetime

#small_pizza_price = 9.99
#medium_pizza_price = 12.99
#large_pizza_price = 17.99
#xlarge_pizza_price = 21.99
#drink_price = 3.99
#breadsticks_price = 6.99
sales_tax_rate = 0.055

PIZZA_SIZE = ("s", "m", "l", "xl")
PIZZA_PRICE = (9.99, 12.99, 17.99, 21.99)

DRINK_PRICE = 3.99
BREADSTICKS_PRICE = 6.99

def main():
    get_order()
    pizza_size()
    calculate()
    receipt()
        
    
def get_order():
    global size, p_quantity, drinks, breadsticks
    size = input("What size pizza would you like? Choose S, M, L, or XL")
    p_quantity = int(input("How many pizzas would you like to order? "))
    drinks = int(input("How many drinks would you like? "))
    breadsticks = int(input("How many orders of breadsticks would you like? "))

def pizza_size():
    global pizza_cost
    if size == "S" or size == "s":
        pizza_cost = PIZZA_PRICE[0]
    elif size == "M" or size == "m":
        pizza_cost = PIZZA_PRICE[1]
    elif size == "L" or size == "l":
        pizza_cost = PIZZA_PRICE[2]
    elif size == "XL" or size == "xl":
        pizza_cost = PIZZA_PRICE[3]


def calculate():
    global p_subtotal, d_subtotal, b_subtotal, subtotal, tax, final_total, size
    for i in range(len(PIZZA_PRICE)):
        if size == PIZZA_SIZE[i]:
            p_subtotal = p_quantity * PIZZA_PRICE[i]
    d_subtotal = drinks * DRINK_PRICE
    b_subtotal = breadsticks * BREADSTICKS_PRICE
    subtotal = p_subtotal + d_subtotal + b_subtotal
    tax = sales_tax_rate * subtotal
    final_total = subtotal + tax

def receipt():
    currency = '8,.2f'
    line = "---------------------------------------"
    date = str(datetime.datetime.now())
    fdate = date[0:16]
    title1 = "**** Palermo Pizza ****"
    title2 = "Local Pizza Done Right!"
    
    print(line)
    print(title1)
    print(title2)
    print(fdate)
    print(line)
    print("Type of Pizza: " + size)
    print("\tQuantity of Pizza(s): " + str(p_quantity))
    print("Price of Pizza(s):      $" + format(p_subtotal, currency))
    print("\tQuantity of Drinks: " + str(drinks))
    print("Price of Drink(s):      $" + format(d_subtotal, currency))
    print("\tQuantity of Breadsticks: " + str(breadsticks))
    print("Price of Breadstick(s): $" + format(b_subtotal, currency))
    print(line)
    print("Sales Tax:              $" + format(tax, currency))
    print("Total:                  $" + format(final_total, currency))
    print(line)
    print(fdate)
main()
