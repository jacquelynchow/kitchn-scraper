import json

# read from json file
with open('kitchnRecipes.json') as json_data:
    jsonData = json.load(json_data) # contains all info scraped (in JSON format)
    
for recipe in jsonData:
    print("Name: " + recipe['name'])
    print("Prep time: " + recipe['prep_time'])
    print("Cook time: " + recipe['cook_time'])
    print("Total time: " + recipe['total_time'])
    print("Servings: " + recipe['servings'])
    print("Course: " + recipe['course'])
    print("Allergens: " + recipe['allergens'])

    ### image??

    print("\nIngredients: ")
    number_ingredients = len(recipe['ingredients'])
    for i in range(number_ingredients):
        print("- " + recipe['ingredients'][i]) # prints each ingredient
    
    print("\nInstructions: ")
    number_step = len(recipe['instructions'])
    for i in range(number_step):
        stepNum = i+1
        print(str(stepNum) + ". " + recipe['instructions'][i]) # prints each ingredient

    print("\nLink: " + recipe['link'])