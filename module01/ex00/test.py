from book import Book
from recipe import Recipe

r1 = Recipe("tart", 2, 1337, ['aa', 'bb', 'cc'], "starter")

b = Book("The Book")
b.add_recipe(r1)

b.get_recipe_by_name('tart')
