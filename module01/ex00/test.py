from book import Book
from recipe import Recipe

try:
    r1 = Recipe('t', 5, 11, ['asdf'], "lunch")
    r2 = Recipe("tt", 5, 0, ['sd'], "lunch", "NOOO")

    b = Book("The Book")
    b.add_recipe(r1)
    b.add_recipe(r2)

    b.get_recipe_by_name('t')
    print(b.get_recipes_by_types('lunch'))


except AssertionError as E:
    print("{}: {}".format(type(E).__name__, E))
