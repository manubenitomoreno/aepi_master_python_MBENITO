from db import session
from models import Recipes

def add_recipe():
    
    recipe_name = input("Enter the recipe name: ")
    
    existing_recipe = session.query(Recipes).filter_by(recipe_name=recipe_name).first()
    
    if existing_recipe:
        print(f"Element {recipe_name} already exists in the database.")
        return


    new_recipe = Recipes(recipe_name=recipe_name)

    session.add(new_recipe)
    session.commit()

    print("Recipe added successfully")
    
if __name__ == '__main__':
    add_recipe()
    #run()
