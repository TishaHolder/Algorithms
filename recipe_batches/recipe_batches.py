#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  min_in = 0

  #set max_batches to a ridiculously high number because it will be used later to compare and set a min value
  max_batches = 10000000

  available_ingredients = None
  recipe_destructued = []
  recipe_destructued = [recipe.values()]
  ingredients_destructured = [ingredients.values()]
  #needed_ingredients_index = len(recipe) - 1


  #divide the ingredient amount by the recipe amount
  #if the answer is less than or equal to zero then return 0
  #if the answer is greater than 0 return the answer
  
  #if the recipe dictionary is longer than the ingredient dictionary
  #we know we don't have enough enough ingredients, so we set max_batches = 0
  if len(recipe) > len(ingredients):
    max_batches = 0
  else:  
    #we iterate through the ingredients dictionary
    #and check if any of the ingredient amounts are less than the recipe amounts
    #if any ingredient qty is less than a recipe qty then max_batches = 0
    for i in ingredients.keys():
      if i in recipe.keys() and ingredients[i] < recipe[i]:     
        max_batches = 0
      else:
        #if all ingredient qtys are less than recipe qtys then calc max_batches by
        #dividing each ingredient qty by each recipe qty
        available_ingredients = ingredients[i] // recipe[i]        

        #find the minimum result after completing all division calculations
        if available_ingredients < max_batches:
           max_batches = available_ingredients          
    
  print(" max_batches %s" %(str( max_batches)))
  return max_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 52, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))