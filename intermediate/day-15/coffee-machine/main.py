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

CHOICE_REPORT = "report"
CHOICE_ESPRESSO = "espresso"
CHOICE_LATTE = "latte"
CHOICE_CAPPUCCINO = "cappuccino"


# Coffee machine
# TODO: 1. Print report
def print_report(resources, money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# TODO: 2. Check resource sufficient?
def check_resource_sufficient(ingredients, resources):
    missing_resource = ""
    for ingredient_name, value in ingredients.items():
        if resources[ingredient_name] < value:
            missing_resource = ingredient_name
            return False, missing_resource

    return True, missing_resource


# TODO: 3. Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


# TODO: 4. Check transaction successful?
def check_transaction_successful():
    pass


def main():
    money = 0
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == CHOICE_REPORT:
            print_report(resources, money)
            continue

        if choice not in [CHOICE_ESPRESSO, CHOICE_LATTE, CHOICE_CAPPUCCINO]:
            print("Not correct choice! Please try again!")
            continue

        drink = MENU[choice]
        ingredients = drink["ingredients"]
        is_resource_sufficient, missing_resource = check_resource_sufficient(ingredients, resources)
        if not is_resource_sufficient:
            print(f"Sorry there is not enough {missing_resource}.")
            is_on = False
            continue

        money_input = process_coins()
        if drink["cost"] > money_input:
            print("Sorry that's not enough money. Money refunded.")

            continue

        money += drink["cost"]
        change = money_input - drink["cost"]
        print(f'Here is ${change} in change.')
        print(f"Here is your {choice} ☕️. Enjoy!")

        # Update resources
        for ingredient_name, ingredient_value in ingredients.items():
            resources[ingredient_name] -= ingredient_value


main()
