from recipe import Recipe
import datetime

class Book:

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name 'name' and returns the instance"""

        for recipe_type in self.recipes_list.keys():
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """

        if recipe_type in self.recipes_list.keys():
            return [recipe.name for recipe in self.recipes_list[recipe_type]]
        return None

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""

        if isinstance(recipe, Recipe):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
