# Make user menu with options
import Ahmad_Ikram
import Lenorris
recipe_list = []

file2 = open("recipes.txt", 'r')
data = file2.readlines()
file2.close()

#user chooses option from menu

while True:
  choice = int(input("Choose a number for the following options.\n1. Add recipe\n2. Edit Recipe\n3. Delete recipe\n4. List all recipes\n5. Search specific recipe\n6. Exit menu"))
  if(choice == 1):
    Ahmad_Ikram.add_recipe(recipe_list)
  elif(choice == 2):
    Ahmad_Ikram.edit_recipe(recipe_list)
  elif(choice == 3):
    Ahmad_Ikram.delete_recipe(recipe_list)
  elif(choice == 4):
    Ahmad_Ikram.list_all_recipes(recipe_list)
  elif(choice == 5):
    selection = int(input("Choose an number for the following options.\n1. Search by Ingredient\n2. Search by cuisine\n3. Search for vegetarian recipes\n4. Search by meal type"))
    if(selection == 1):
      Lenorris.search_by_ingredient(recipe_list)
    elif(selection == 2):
      Lenorris.search_by_cuisine(recipe_list)
    elif(selection == 3):
      Lenorris.search_by_vegetarian(recipe_list)
    elif(selection == 4):
      Lenorris.search_by_meal_type(recipe_list)
  elif(choice == 6):
    break

#write recipes to file
file1 = open("recipes.txt", 'w+')
data = str(recipe_list)
file1.write(data)
file1.close()




  

