cashier = input("Cashier Name: ")
menu = ["Yum Burger Value Meal [Y1]", "Yum Burger Cheese Value Meal [Y2]", "Bacon Cheese Yumburger Meal [Y3]", "Yumburger Cheese Deluxe Meal [Y4]", "Bacon Deluxe Cheese Yumburger Meal [Y5]", "Amazing Aloha Yumburger Value Meal [Y6]", "Yum Burger Champ Value Meal [Y7]", "Bacon Champ Value Meal [Y8]", "Amazing Aloha Champ Value Meal [Y9]", "1 pc Burger Steak w/ Drink [B1]", "2 pc Burger Steak w/ Drink [B2]", "1 pc Burger Steak with 3 pcs Shanghai w/ Drink [B3]", "1 pc Burger Steak w/ Fries & Drink [B4]", "Ultimate Burger Steak w/ Egg Meal & Drink", "Ultimate Burger Steak w/o Egg Meal & Drink", "Burger Steak Family Pan 6pcs [B7]", "Burger Steak Family Pan 8pcs [B8]", "Jolly Hotdog Cheesy Classic w/ Drink [H1]", "Jolly Hotdog Cheesy Classic w/ Fries & Drink [H2]", "Jolly Hotdog Cheesy Classic w/ Fries & Float [H3]", "Jolly Spaghetti w/ Drink [S1]", "Jolly Spaghetti w/ Fries & Drink [S2]", "Jolly Spaghetti w/ Yumburger & Drink [S3]", "Jolly Spaghetti w/ Cheesy Yumburger & Drink [S4]", "Jolly Spaghetti w/ Burger Steak & Drink [S5]", "1 pc Chickenjoy w/ Rice & Drink [C1]", "1 pc Chickenjoy w/ Double Rice & Drink [C2]", "1 pc Chickenjoy w/ Jolly Spaghetti & Drink [C3]", "1 pc Chickenjoy w/ Palabok & Drink [C4]", "2 pcs Chickenjoy w/ Rice & Drink [C5]", "1 pc Chickenjoy w/ Rice, Fries & Drink [C6]", "6 pc Chickenjoy Bucket", "8 pc Chickenjoy Bucket", "Family Meal A – 6 pieces Chickenjoy Bucket, 3 rice, 3 sides, 3 sundaes, 3 drinks", "Family Meal A – 8 pieces Chickenjoy Bucket, 4 rice, 4 sides, 4 sundaes, 4 drinks", "Family Meal B – 6 pieces Chickenjoy Bucket, 3 spaghetti, 3 rice, 3 drinks", "Family Meal B – 8 pieces Chickenjoy Bucket, 4 spaghetti, 4 rice, 4 drinks", "Jolly Crispy Fries (Regular)", "Jolly Crispy Fries (Large)", "Jolly Crispy Fries (Jumbo)", "1 pc Original Tuna Pie w/ Fries & Drink [P2]", "1pc Peach Mango Pie (Solo)", "1pc Buko Pie (Solo)", "1pc Ube Macapuno Pie (Solo)", "Yum Burger with Reg. Pineapple Juice + Toy", "Jolly Spaghetti with Reg. Pineapple Juice + Toy", "1 pc Chickenjoy with Reg. Pineapple Juice + Toy", "Burger Steak with Reg. Pineapple Juice + Toy", "2 pc Pancake w/ Drink", "Hotdog w/ Garlic Rice, Fried Egg & Drink", "Breakfast Burger Steak w/ Garlic Rice, Fried Egg & Drink", "Beef Tapa w/ Garlic Rice, Fried Egg & Drink", "Corned Beef w/ Garlic Rice, Fried Egg & Drink", "Longganisa w/ Garlic Rice, Fried Egg & Drink", "Bacon, Egg & Cheese Pancake Sandwich w/ Drink", "Egg & Cheese Pancake Sandwich w/ Drink", "Egg & Cheese Sandwich w/ Drink", "Chocolate Sundae Twirl", "Coke, Sarsi or Royal Floats", "Vanilla Cone Twirl", "Chocolate Cone Twirl", "Mini Sundae Twirl"]
price = [86.00, 96.00, 110.00, 120.00, 130.00, 135.00, 195.00, 230.00, 245.00, 65.00, 90.00, 109.00, 79.0, 190.00, 175.00, 255.00, 339.00, 80.00, 120.00, 125.00, 65.00, 95.00, 95.00, 110.00, 99.00, 95.00, 99.00, 125.00, 175.00, 170.00, 105.00, 399.00, 499.00, 599.00, 799.00, 550.00, 799.00, 42.00, 60.00, 75.00, 89.00, 30.00, 30.00, 30.00, 110.00, 116.00, 157.00, 116.00, 83.00, 109.00, 109.00, 142.00, 142.00, 142.00, 88.00, 77.00, 72.00, 30.00, 37.00, 10.00, 15.00, 26.00]
order = []
quantity = []
order_price = []

print("Welcome to Jollibee!")
print("Menu:")
for i in range(len(menu)):
    print(str(i+1) + ". " + menu[i] + " - " + str(price[i]))

while True:
    try:
        order_num = int(input("What would you like to order?: "))
        if order_num > 0 and order_num <= len(menu):
            order.append(menu[order_num-1])
            order_price.append(price[order_num-1])
            print("Added " + menu[order_num-1] + " to your order.")
            print("Your order: " + str(order))
            print("Your order price: " + str(order_price))
            quantity_item = int(input("How much do you want to buy?: "))
            quantity.append(quantity_item)
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")
    if input("Would you like to order more? (y/n) ") == "n":
        break

total = 0

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print("")
print("-" * 80)
print("JBO766")
print("CUSTOMER COPY")
print("Cashier: ", cashier)
print("-" * 80)
print(dt_string)
print("-" * 80)
for i in range(len(order)):
    print(f"{quantity[i]} {order[i]} for {order_price[i]} each")
    total += quantity[i] * order_price[i]

print("")
print(f"Total: {total}")
print("*" * 80)

print("Tell us about your experience.")
print("Send us feedback at bit.ly/jfccaresph")
print("Visit us also at www.jollibee.com.ph")

print("This serves as an OFFICIAL RECEIPT")
print("ANSI Information Systems, Inc.")
print("Tytana St., Manila")
print("VAT Reg TIN: 000-330-515-000")
print("ACCREDITATION NO.03000033051500000712638")
print("Date Issued: 04/16/2007")
print("Valid Until: 07/31/2025")
print("PTU No. FP102017-125-0141900-00095")
print("Date Issued: 10/19/2017")


