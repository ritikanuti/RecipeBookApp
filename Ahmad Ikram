# An empty list of recipes(Dictionaries)
recipes = []

# Add a New Recipe
def add_recipe(recipe_list):
    print("\n Add a New Recipe \n")

    # Takes innput as variables
    name = input("Recipe name: ")
    ingredients_input = input("Ingredients (comma-separated): ")
    instructions = input("Instructions: ")

    cuisine = input("Cuisine (e.g., Italian, Indian, etc.): ")
    meal_type = input("Meal type (breakfast/lunch/dinner): ")
    prep_time = int(input("Preparation time (in minutes): "))
    is_vegetarian_input = input("Is it vegetarian? (yes/no): ")
   # Converting is vegitarian as a boolean
    is_vegetarian = is_vegetarian_input.lower() == "yes"

    # Assigns an ID
    new_id = len(recipe_list) + 1

    # Creates the recipe dictionary
    new_recipe = {
        "id": new_id,
        "name": name,
        "ingredients": ingredients_input,
        "instructions": instructions,
        "cuisine": cuisine,
        "meal_type": meal_type,
        "prep_time": prep_time,
        "is_vegetarian": is_vegetarian
    }

    # Adds the recipe to the list
    recipe_list.append(new_recipe)
    print(" Recipe added successfully!")


# 2. Edit an Existing Recipe

def edit_recipe(recipe_list):
    print("\n Edit a Recipe \n")
    recipe_id = int(input("Enter the ID of the recipe to edit: "))


    for recipe in recipe_list:
        if recipe["id"] == recipe_id:
            print("Leave blank to keep it unchanged.\n")
        # only changes values if an input is provided
        print("Current name: " + recipe["name"])
        name_input = input("New name (leave blank to keep): ")
        if name_input != "":
            name = name_input
        else:
            name = recipe["name"]

        print("Current ingredients: " + recipe["ingredients"])
        ingredients_input = input("New ingredients , leave blank to keep): ")
        if ingredients_input != "":
            ingredients = ingredients_input
        else:
            ingredients = recipe["ingredients"]

        print("Current instructions: " + recipe["instructions"])
        instructions_input = input("New instructions (leave blank to keep): ")
        if instructions_input != "":
            instructions = instructions_input
        else:
            instructions = recipe["instructions"]


        print("Current cuisine: " + recipe["cuisine"])
        cuisine_input = input("New cuisine (leave blank to keep): ")
        if cuisine_input != "":
            cuisine = cuisine_input
        else:
            cuisine = recipe["cuisine"]

        print("Current meal type: " + recipe["meal_type"])
        meal_type_input = input("New meal type (leave blank to keep): ")
        if meal_type_input != "":
            meal_type = meal_type_input
        else:
            meal_type = recipe["meal_type"]


        print("Current prep time: " + str(recipe["prep_time"]) + " minutes")
        prep_time_input = input("New prep time (in minutes, leave blank to keep): ")
        
        
        if prep_time_input != "":
            prep_time = int(prep_time_input)
        else:
            prep_time = recipe["prep_time"]

        if recipe["is_vegetarian"]:
            print("vegetarian : Yes")
        else:
            print("vegetarian : No")
        is_vegetarian_input = input("Is it vegetarian? (yes/no, leave blank to keep): ")
        if is_vegetarian_input != "":
            is_vegetarian = is_vegetarian_input.lower() == "yes"
        else:
            is_vegetarian = recipe["is_vegetarian"]
        # Updates the values
        recipe["name"] = name
        recipe["ingredients"] = ingredients
        recipe["instructions"] = instructions
        recipe["cuisine"] = cuisine
        recipe["meal_type"] = meal_type
        recipe["prep_time"] = prep_time
        recipe["is_vegetarian"] = is_vegetarian

        print("Recipe updated")
        return

    print("Recipe not found with that ID")
# deleting
def delete_recipe(recipe_list):
    print("\nDelete a Recipe \n")
    recipe_id = int(input("Enter the ID of the recipe to delete: "))


    for recipe in (recipe_list):
        if recipe["id"] == recipe_id:
            # Confirmation before deleting
            Confirmation = input("Are you sure , You want to delete :" + recipe["name"] + "?\n \"Confirm\" to continue\n").lower
            if Confirmation == "confirm":

                recipe_list.remove(recipe)
                print(" Recipe deleted successfully.")
                return
            else:
                print("Recipe Not Deleted")
                break

    print("No recipe found with that ID")

#Shows the whole list od recipes

def list_all_recipes(recipe_list):
    print("\n All Recipes \n")
    for recipe in recipe_list:
        print("ID: " + str(recipe["id"]))
        print("Name: " + recipe["name"])
        print("Cuisine: " + recipe["cuisine"])
        print("Meal Type: " + recipe["meal_type"])
        print("Prep Time: " + str(recipe["prep_time"]) + " minutes")



    if recipe["is_vegetarian"]:
        print("Vegetarian: Yes")
    else:
        print("Vegetarian: No")




# Pleasse delete all after this
Boiled_Egg ={
    "id": 1,
    "name": "Boiled Egg",
    "ingredients": "Egg Water",
    "instructions": "Boil the egg",
    "cuisine": "idk",
    "meal_type": "breakfast",
    "prep_time": 10,
    "is_vegetarian": True
}
recipes.append(Boiled_Egg)
x=int(input("menu"))
if x==1:
    add_recipe(recipes)
    list_all_recipes(recipes)
elif x==2:
    edit_recipe(recipes)
    list_all_recipes(recipes)
elif x==3:
    list_all_recipes(recipes)
    list_all_recipes(recipes)
elif x==4:
    delete_recipe(recipes)
    list_all_recipes(recipes)

