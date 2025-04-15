# Make user menu with options
import Ahmad_Ikram

file2 = open("recipes.txt", 'r')
data = file2.read()
recipes = data
print(recipes)
#user chooses option from menu

while True:
  choice = int(input("Choose a number for the following options.\n1. Add recipe\n2. Edit Recipe\n3. Delete recipe\n4. List all recipes\n5. exit menu"))
  if(choice == 1):
    Ahmad_Ikram.add_recipe(recipes)
  elif(choice == 2):
    Ahmad_Ikram.edit_recipe(recipes)
  elif(choice == 3):
    Ahmad_Ikram.delete_recipe(recipes)
  elif(choice == 4):
    Ahmad_Ikram.list_all_recipes(recipes)
  elif(choice == 5):
    break



#write recipes to file
file1 = open("recipes.txt", 'w')
recipeStr = str(recipes)
file1.write(recipeStr)
file1.close()


  

