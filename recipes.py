from yaml import dump, load, safe_load

def convert_to_markdown(recipe_yaml, out_dir):
    with open(recipe_yaml, 'r') as file:
        recipe = safe_load(file)
    name = recipe['name']
    outname = out_dir + "/" + name.replace(" ", "_") + ".md"
    out = open(outname, "w")
    print("#", name) 
    out.write("#" + name + "\n\n")
    print(recipe['description'])
    out.write(recipe['description'] + "\n")
    subsection("Ingredients", "bullet", recipe['ingredients'], out)
    subsection("Steps", "number", recipe['steps'], out)
    subsection("Options", "bullet", recipe['optional'], out)
    file.close()

def subsection(title, list_type, info, handle):
    print("##", title, "\n")
    handle.write("##" + title + "\n")
    if list_type == "bullet":
        for item in info:
            print("*", item)
            handle.write("*" + item + "\n")
    elif list_type == "number":
        count = 0
        for item in info:
            print(str(count) + ".", item)
            handle.write(str(count) + "." + item + "\n")
            count = count + 1
    print("\n")
    handle.write("\n")
    return

if __name__ == "__main__":
    recipe_file = "recipes/tacos.yaml"
    out_dir = "cookbook"
    convert_to_markdown(recipe_file, out_dir)
