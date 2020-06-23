from bs4 import BeautifulSoup # library to parse opened html
import requests # library to open urls
import json

link = "https://minimalistbaker.com/3-ingredient-chocolate-fudge-dairy-free/"
response = requests.get(link).content
content = BeautifulSoup(response, "html.parser") # root of the parsed tree of our html page

'''
Note: 
- cook time is only available for some recipes 
- votes_container is the rating of the recipe from online users  
'''
# containers
recipe_container = content.find("div", {"class": "wprm-recipe-container"})
preptime_container = content.find("div", {"class": "wprm-recipe-block-container wprm-recipe-block-container-columns wprm-block-text-normal wprm-recipe-time-container wprm-recipe-prep-time-container"})
cooktime_container = content.find("div", {"class": "wprm-recipe-block-container wprm-recipe-block-container-columns wprm-block-text-normal wprm-recipe-time-container wprm-recipe-cook-time-container"})
totaltime_container = content.find("div", {"class": "wprm-recipe-block-container wprm-recipe-block-container-columns wprm-block-text-normal wprm-recipe-time-container wprm-recipe-total-time-container"})
ingredients_container = content.find("div", {"class": "wprm-recipe-ingredient-group"})
instructions_container = content.find("div", {"class": "wprm-recipe-instruction-group"})
#votes_container = content.find("div", {"class": "wprm-recipe-rating wprm-recipe-rating-separate"})

# grab ingredients from div
ingredients = [item.text for item in ingredients_container.find_all("li")]

# grab instructions from div
instructions = [step.text for step in instructions_container.find_all("li")]

recipeArr = []
# recipe object
recipeObject = {
    "link": link,
    "name": recipe_container.find("h2", {"class": "wprm-recipe-name wprm-block-text-bold"}).text,
    "prep_time": preptime_container.find("span", {"class": "wprm-recipe-time wprm-block-text-normal"}).text,
    "cook_time": cooktime_container.find("span", {"class": "wprm-recipe-time wprm-block-text-normal"}).text,
    "total_time": totaltime_container.find("span", {"class": "wprm-recipe-time wprm-block-text-normal"}).text,
    "image": content.find("figure", {"class": "wp-block-image size-full"}).img["src"],
    "servings": content.find("span", {"class": "wprm-recipe-servings-with-unit"}).text,
    "course": content.find("span", {"class": "wprm-recipe-course wprm-block-text-normal"}).text,
    "allergens": content.find("span", {"class": "wprm-recipe-cuisine wprm-block-text-normal"}).text,
    "ingredients": ingredients,
    "instructions": instructions
}
recipeArr.append(recipeObject) 
with open('kitchnRecipes.json', 'w') as outfile: json.dump(recipeArr, outfile)  

# testing
#print(recipeObject)
