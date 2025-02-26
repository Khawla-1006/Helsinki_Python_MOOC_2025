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


            
if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)