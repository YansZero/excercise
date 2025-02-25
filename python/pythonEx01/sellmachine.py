menu = {
    "pizza": 300,
    "popcorn": 200,
    "frenchFries": 90,
    "chips": 70,
    "coke": 60,
    "lemonJuice": 65
}
total = 0
cart = []

print("---------Menu---------")
for item, price in menu.items():
    print(f"{item}: {price}")

while True:
    food = input("please key in the item you want(q is quite):")
    if food == "q":
        break
    elif menu.get(food) is None:
        print("No item match!")
    else:
        cart.append(food)
        total += menu.get(food)

print("---------Cart--------")
for item in cart:
    print(f"you buy: {item}", end=" \n")

print(f"total is: {total:.2f}")
