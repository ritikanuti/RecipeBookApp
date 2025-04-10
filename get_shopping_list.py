def get_shopping_list(recipe):
    # This function takes in a recipe and prints a list of ingredients for shopping
    
    print("Shopping List:")
    
    # Loop through each ingredient in the recipe
    for item in recipe["ingredients"]:
        # Format the quantity, unit, and name of the ingredient
        print(f"- {item['quantity']} {item['unit']} of {item['name']}")
