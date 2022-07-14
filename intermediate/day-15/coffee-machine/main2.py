MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

CHOICE_OFF = "off"
CHOICE_REPORT = "report"
CHOICE_ESPRESSO = "espresso"
CHOICE_LATTE = "latte"
CHOICE_CAPPUCCINO = "cappuccino"
profit = 0

# Coffee machine
# TODO: 1. Print report
def print_report(resources, profit):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# TODO: 2. Check resource sufficient?
def check_resource_sufficient(ingredients, resources):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


# TODO: 3. Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


# TODO: 4. Check transaction successful?
def check_transaction_successful(drink_cost, money_input):
    if drink_cost > money_input:
        print("Sorry that's not enough money. Money refunded.")
        return False

    global profit
    profit += drink_cost
    change = money_input - drink_cost
    print(f'Here is ${change} in change.')

    return True


def make_coffee(choice, ingredients):
    print(f"Here is your {choice} ☕️. Enjoy!")

    # Update resources
    for ingredient_name, ingredient_value in ingredients.items():
        resources[ingredient_name] -= ingredient_value


def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == CHOICE_REPORT:
            print_report(resources, profit)
            continue

        if choice == CHOICE_OFF:
            is_on = False
            continue

        if choice not in [CHOICE_ESPRESSO, CHOICE_LATTE, CHOICE_CAPPUCCINO]:
            print("Not correct choice! Please try again!")
            continue

        drink = MENU[choice]
        ingredients = drink["ingredients"]
        if not check_resource_sufficient(ingredients, resources):
            is_on = False
            continue

        money_input = process_coins()
        check_transaction_successful(drink["cost"], money_input)
        make_coffee(choice, ingredients)

main()
