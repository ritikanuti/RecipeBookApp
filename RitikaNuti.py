# Make user menu with options
import Ahmad_Ikram
#user chooses option from menu
recipes = []
choice = int(input("Choose a number for the following options.\n1. Add recipe\n2. Edit Recipe\n3. Delete recipe\n4. List all recipes"))
if(choice == 1):
  Ahmad_Ikram.add_recipe(recipes)
elif(choice == 2):
  Ahmad_Ikram.edit_recipe(recipes)
elif(choice == 3):
  Ahmad_Ikram.delete_recipe(recipes)
elif(choice == 4):
  Ahmad_Ikram.list_all_recipes(recipes)

#write recipes to file
file1.open("recipes.txt",'w')
file1.write(recipes)
file1.close()


  

