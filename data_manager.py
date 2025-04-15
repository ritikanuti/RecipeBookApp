# data_manager.py
# This file handles saving and loading recipes using a simple text file.

# Name of the file where we store recipes
FILE_PATH = "recipes.txt"

# This function loads recipes from the file into a list
def load_recipes():
    recipes = []  # this will hold all recipes

    try:
        # Open the file to read
        f = open(FILE_PATH, "r")
        lines = f.readlines()
        f.close()

        recipe = {}  # start with an empty recipe

        # Go through every line in the file
        for line in lines:
            line = line.strip()  # remove spaces and newlines

            if line == "":
                # If it's an empty line, we assume one recipe has ended
                if "name" in recipe:
                    recipes.append(recipe)  # add the finished recipe
                recipe = {}  # start a new one
            else:
                # Otherwise, read key and value from the line
                if ":" in line:
                    key, value = line.split(":", 1)  # split only once
                    key = key.strip()
                    value = value.strip()

                    # Convert values to the right type
                    if key == "id" or key == "prep_time":
                        recipe[key] = int(value)
                    elif key == "is_vegetarian":
                        recipe[key] = value.lower() == "true"
                    else:
                        recipe[key] = value

        # If the last recipe doesn't end with a blank line, add it
        if "name" in recipe:
            recipes.append(recipe)

    except:
        # If file doesn't exist or there's a problem, just return an empty list
        recipes = []

    return recipes  # return the list of recipes

# This function saves all recipes into the file
def save_recipes(recipes):
    f = open(FILE_PATH, "w")  # open the file to write (this clears old data)

    # Go through each recipe in the list
    for r in recipes:
        f.write("id: " + str(r["id"]) + "\n")
        f.write("name: " + r["name"] + "\n")
        f.write("ingredients: " + r["ingredients"] + "\n")
        f.write("instructions: " + r["instructions"] + "\n")
        f.write("cuisine: " + r["cuisine"] + "\n")
        f.write("meal_type: " + r["meal_type"] + "\n")
        f.write("prep_time: " + str(r["prep_time"]) + "\n")
        f.write("is_vegetarian: " + str(r["is_vegetarian"]) + "\n")
        f.write("\n")  # separate recipes with a blank line

    f.close()  # close the file when done
