import csv

from models.dish import Dish
from models.ingredient import Ingredient


def create_menu(path):
    result = set()
    dishes_dict = {}

    with open(path, encoding = "utf-8") as file:
        for line in csv.DictReader(file):
            dish, price, ingredient, recipe_amount = line.values()
            if dish in result:
                new_ingredient = Ingredient(ingredient)
                dishes_dict[dish].add_ingredient_dependency(
                    new_ingredient, int(recipe_amount))
            else:
                new_dish = Dish(dish, float(price))
                new_ingredient = Ingredient(ingredient)
                new_dish.add_ingredient_dependency(
                    new_ingredient, int(recipe_amount))
                dishes_dict[dish] = new_dish
                result.add(dish)

    result = set(dishes_dict.values())
    return result


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = create_menu(source_path)
