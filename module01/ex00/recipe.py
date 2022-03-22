class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=None):
        assert type(name) == str, "recipe name must be of type 'str'."
        assert len(name), "recipe name must not be empty."
        assert type(cooking_lvl) == int, "cooking level must be of type 'int'."
        assert 1 <= int(cooking_lvl) <= 5, "cooking level must be between 1 and 5."
        assert type(cooking_time) == int, "cooking time must be of type 'int'."
        assert int(cooking_time) >= 0, "cooking time must be a positive number."
        assert type(ingredients) == list and len(ingredients), "ingredients must be a non-empty list."
        assert type(recipe_type) == str and len(recipe_type), "recipe type must be non-empty string"
        assert recipe_type in ("starter", "lunch", "dessert"), "recipe type must be 'starter', 'lunch' or 'dessert'."
        assert description is None or type(description) == str, "Invalid description."

        for ing in ingredients:
            assert type(ing) == str and len(ing), "ingredients must be non-empty strings."

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""

        txt = "Name: {}\nLevel: {}\nCooking time: {}min\nIngredients: {}\nRecipe type: {}".format(
            self.name,
            self.cooking_lvl,
            self.cooking_time,
            self.ingredients,
            self.recipe_type)

        if self.description is not None:
            txt += "\nDescription: {}".format(self.description)

        return txt
