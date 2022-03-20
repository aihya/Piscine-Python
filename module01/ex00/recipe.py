def isinteger(string):
    if len(string) and string[0] in "+-":
        if string[1:].isnumeric():
            return True
    elif len(string) and string.isnumeric():
        return True
    return False


class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
        assert type(name) == str, "recipe name must be of type 'str'."
        assert len(name), "recipe name must not be empty."
        assert type(cooking_lvl) == int, "cooking level must be of type 'int'."
        assert 1 <= int(cooking_lvl) <= 5, "cooking level must be between 1 and 5."
        assert type(cooking_time) == int, "cooking time must be of type 'int'."
        assert int(cooking_time) >= 0, "cooking time must be a positive number."
        assert type(ingredients) == list, "ingredients must be a 'list'"
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""

        txt = "Name: {}\nLevel: {}\nCooking time: {}min\nIngredients: {}\nDescription: {}\nRecipe type\n{}".format(
            self.name,
            self.cooking_lvl,
            self.cooking_time,
            self.ingredients,
            self.description,
            self.recipe_type)

        return txt
