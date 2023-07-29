from db import session
from models import Relations, Recipes, Elements

def add_relation():
    
    recipe_name = input("Enter the recipe name: ")
    element_name = input("Enter the element name: ")
    
    # Check if the recipe exists
    recipe = session.query(Recipes).filter_by(recipe_id=recipe_name).first()
    if not recipe:
        print("Recipe does not exist.")
        return

    # Check if the element exists
    element = session.query(Elements).filter_by(element_id=element_name).first()
    if not element:
        print("Element does not exist.")
        return

    # Check if the element is already related to the recipe
    existing_relation = (
        session.query(Relations)
        .filter_by(recipe_name=recipe_name, element_id=element_name)
        .first()
    )
    if existing_relation:
        print("Relation already exists.")
        return

    new_relation = Relations(recipe_name=recipe_name, element_id=element_name)
    session.add(new_relation)
    session.commit()

    print("Relation added successfully.")

if __name__ == "__main__":
    add_relation()
