#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    """
    Loop through the recipe list and grab the amount of each item
    and compare it with the ingredients. If we do not have the ingredients
    return 0 since no batches can be made. Else, return the amount of batches
    that can be made with the ingredients.
    """
    item_batch_count = []

    for item in recipe:

        if item not in ingredients:
            return 0
        elif ingredients[item] // recipe[item] >= 1:
            """
            Because when we return an item, it stops the program from running.
            We need to add a list of possible times and return that value
            """
            batch_count = ingredients[item] // recipe[item]
            item_batch_count.append(batch_count)
        else:
            return 0
    return min(item_batch_count)

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: "
          .format(batches=recipe_batches(recipe, ingredients)) +
          "{ingredients}.".format(ingredients=ingredients))
