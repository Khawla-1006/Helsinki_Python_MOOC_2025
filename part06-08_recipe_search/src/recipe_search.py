# Write your solution here
def recipe_maker(file: str):
    h =[]
    r =[]
    recipes = []
    with open(file) as content :
        for line in content :
            l = line.replace("\n","")
            h.append(l)
        h.append("")
        for item in h :
            if item != "" :
                r.append(item)
            else :
                recipes.append(r)
                r = []
    return recipes

def search_by_name(filename: str, word: str):
    names = []
    found = []
    recipes = recipe_maker(filename)
    for recipe in recipes :
        names.append(recipe[0])
    for name in names :
        if word.lower() in name.lower() :
            found.append(name)
    return found

def search_by_time(filename: str, prep_time: int):
    times = []
    found_time = []
    recipes = recipe_maker(filename)
    for recipe in recipes:
        time = (recipe[0],int(recipe[1]))
        times.append(time)
    for item in times :
        if item[1] <= prep_time+5  :
            res = f"{item[0]}, preparation time {item[1]} min"
            found_time.append(res)
    return found_time


def search_by_ingredient(filename: str, ingredient: str) :
    found = []
    ing = []
    recipes = recipe_maker(filename)
    for recipe in recipes :
        ing.append((recipe[0],int(recipe[1]),recipe[2:]))
    for i in ing :
        if ingredient in i[2]:
            res = f"{i[0]}, preparation time {i[1]} min"
            found.append(res)
    return found



    
if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)