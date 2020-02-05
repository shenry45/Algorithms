#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # track number of possible batches
  ingredient_counts = []

  # check if all ingredients are available
  for ingredient in recipe:
    # if not available
    if ingredient in ingredients:
      pass
    else:
      return 0

  # run for all available ingredients
  for ingredient in ingredients:
    # if ingredient is not found pass
    if recipe[ingredient] == False:
      pass
    # else how many of current is divisible by recipe
    else:
      if (ingredients[ingredient] / recipe[ingredient]) < 1:
        return 0
      # else return current ingredient // recipe ingredient
      else:
        ingredient_counts.append(ingredients[ingredient] // recipe[ingredient])

  # find min of batch list
  return min(ingredient_counts)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))