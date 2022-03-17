cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

def delete_recipe(name):
    if name in cookbook.keys():
        del cookbook[name]

def print_recipe(name):
    if name in cookbook.keys():
        print("\nRecipe for {}:".format(name))
        print("Ingredients list: {}.".format(cookbook[name]["ingredients"]))
        print("To be eaten for {}.".format(cookbook[name]["meal"]))
        print("Takes {} minutes of cooking.\n".format(cookbook[name]["prep_time"]))
    else:
        print("\nRecipe {} not found in the CookBook.\n".format(name))

def print_recipes():
    print("\nAll recipes:")
    print("{}\n".format('\n'.join(list(cookbook.keys()))))

if __name__ == "__main__":
    while True:
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        command = input(">> ")

        try:
            command = int(command)

            if command == 1:
                name = ""
                while len(name) == 0:
                    name = input(">> Name: ")

                ingredients = []
                count = 1
                while True:
                    ingredient = input(">> Ingredient {}: ".format(count))
                    if len(ingredient) == 0:
                        break
                    ingredients.append(ingredient)
                    count += 1

                meal = ""
                while len(meal) == 0:
                    meal = input(">> Meal: ")

                while True:
                    try:
                        prep_time = int(input(">> Preperation time: "))
                        if (prep_time < 0):
                            raise ValueError
                        break
                    except ValueError:
                        pass
                add_recipe(name, ingredients, meal, prep_time)

            elif command == 2:
                name = ""
                while len(name) == 0:
                    name = input(">> Name: ")
                delete_recipe(name)

            elif command == 3:
                print("\nPlease enter the recipe's name to get its details:")
                name = ""
                while len(name) == 0:
                    name = input(">> Name: ")
                print_recipe(name)

            elif command == 4:
                print_recipes()

            elif command == 5:
                break
            
            else:
                print("\nThis options does not exist.\n")
        except AssertionError as e:
            print(e)
        except ValueError as e:
            continue
