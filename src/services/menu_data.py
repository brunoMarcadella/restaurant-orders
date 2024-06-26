import csv
from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')

            dishes = dict()

            for row in reader:
                if row["dish"] not in dishes:
                    dish = Dish(row["dish"], float(row["price"]))
                    ingredient = Ingredient(row["ingredient"])
                    dish.add_ingredient_dependency(
                        ingredient, int(row["recipe_amount"])
                    )
                    dishes[row["dish"]] = dish
                else:
                    ingredient = Ingredient(row["ingredient"])
                    dishes[row["dish"]].add_ingredient_dependency(
                        ingredient, int(row["recipe_amount"])
                    )

            self.dishes = set(dishes.values())


data = MenuData("tests/mocks/menu_base_data.csv")
print(data.dishes)
