# Make user menu with options
import Ahmad_Ikram
import Lenorris
recipes = []

file2 = open("recipes.txt", 'r')
data = file2.readlines()
file2.close()

#user chooses option from menu

while True:
  choice = int(input("Choose a number for the following options.\n1. Add recipe\n2. Edit Recipe\n3. Delete recipe\n4. List all recipes\n5. Search specific recipe\n6. Exit menu"))
  if(choice == 1):
    Ahmad_Ikram.add_recipe(recipes)
  elif(choice == 2):
    Ahmad_Ikram.edit_recipe(recipes)
  elif(choice == 3):
    Ahmad_Ikram.delete_recipe(recipes)
  elif(choice == 4):
    Ahmad_Ikram.list_all_recipes(recipes)
  elif(choice == 6):
    break

#write recipes to file
file1 = open("recipes.txt", 'w+')
numLines = len(file1.readlines())
for i in range(1,numLines):
  file1.write(recipes[i])
file1.close()




  

