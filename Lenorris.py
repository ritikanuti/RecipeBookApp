# Search by Ingredient
def search_by_ingredient(recipe_list):
    print("\n Search by Ingredient \n")
    keyword = input("Enter an ingredient to search: ").lower()

    found = False
    for recipe in recipe_list:
        if keyword in recipe["ingredients"].lower():
            print("Found in:", recipe["name"])
            found = True

    if not found:
        print("No recipes found with that ingredient.")

# Search by Cuisine
def search_by_cuisine(recipe_list):
    print("\n Search by Cuisine \n")
    cuisine = input("Enter the cuisine (e.g., Italian): ").lower()

    found = False
    for recipe in recipe_list:
        if recipe["cuisine"].lower() == cuisine:
            print("Found:", recipe["name"])
            found = True

    if not found:
        print("No recipes found for that cuisine.")

# Search by Vegetarian
def search_by_vegetarian(recipe_list):
    print("\n Search for Vegetarian Recipes \n")

    found = False
    for recipe in recipe_list:
        if recipe["is_vegetarian"]:
            print("Found:", recipe["name"])
            found = True

    if not found:
        print("No vegetarian recipes found.")

# Search by Meal Type
def search_by_meal_type(recipe_list):
    print("\n Search by Meal Type \n")
    meal_type = input("Enter the meal type (breakfast/lunch/dinner): ").lower()

    found = False
    for recipe in recipe_list:
        if recipe["meal_type"].lower() == meal_type:
            print("Found:", recipe["name"])
            found = True

    if not found:
        print("No recipes found for that meal type.")
