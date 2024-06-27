from csv import DictReader
from typing import Dict


from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        ingrediente = list(recipe.keys())[0]

        if ingrediente not in self.inventory:
            print(f"Ingrediente {ingrediente} não está no inventário")
            return False

        if (
            int(self.inventory[ingrediente]) < int(list(recipe.values())[0])
            or len(list(recipe)) > 1
        ):
            return False
        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        for ingredient in list(recipe.items()):
            dicionario = dict()
            dicionario[ingredient[0]] = ingredient[1]
            if self.check_recipe_availability(dicionario):
                result = self.inventory[ingredient[0]] - ingredient[1]
                self.inventory[ingredient[0]] = result

            else:
                raise ValueError
        return None
