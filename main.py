"""docstring"""
import json

def adjust_recipe(recipe, num):
    new_recipe = recipe
    print(new_recipe)
    new_recipe["servings"] = num
    print(new_recipe)
    new_recipe["ingredients"]["Spaghetti"] = new_recipe["ingredients"]["Spaghetti"] / 4 * num
    new_recipe["ingredients"]["Tomato Sauce"] = new_recipe["ingredients"]["Tomato Sauce"] / 4 * num
    new_recipe["ingredients"]["Minced Meat"] = new_recipe["ingredients"]["Minced Meat"] / 4 * num
    return new_recipe


def load_recipe(recipe):
    recipe_dict = json.loads(recipe)
    return recipe_dict

if __name__ == "__main__":
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    print(adjust_recipe(recipe_json, 2))
