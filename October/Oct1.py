def get_topping_one(pizza_order):
    return pizza_order[0:6]

def get_topping_two(pizza_order):
    return pizza_order[1:8]

def get_price(pizza_order):
    Dollars = (int(pizza_order[3:4])/100)
    return Dollars

def too_much_cheese(pizza_order):
    if pizza_order[0:6] == "cheese":
        return True
    else:
        return False

def full_order(pizza_order):
    if too_much_cheese(pizza_order) == True:
        return "That's a lot of cheese!"
    if too_much_cheese(pizza_order) == False and int(get_price(pizza_order) == 45):
        return "Wow that's an expensive pizza!"
    if get_topping_two(pizza_order) == "pineapple":
        return "Pineapple DOES belong on pizza."
    elif get_topping_two(pizza_order) == "artichoke":
        return "That's an interesting combo."
    if int(get_price(pizza_order) < 12) or int(get_price(pizza_order) == 50):
        return "Are we sure they're charging us right?"
    else:
        return "Now that's a smokin' deal! Give me more!"


def run():
    print(get_topping_one("cheese, pepperoni, 3000"))
    print(get_topping_one("olives, pepperoni, 3000"))
    print(get_topping_two("cheese, pepperoni, 3000"))
    print(get_price("cheese, pepperoni, 3000"))
    print(too_much_cheese("cheese, pepperoni, 3000"))
    #create your own tests here
    return # make sure this line is last

if __name__ == "__main__":
    run()
