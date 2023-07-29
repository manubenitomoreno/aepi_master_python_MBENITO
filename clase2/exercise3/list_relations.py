from db import session
from models import Relations, Recipes, Elements

def list_relations():
    relations = session.query(Relations).all()

    if not relations:
        print("No relations found.")
        return

    print("Relations:")
    for relation in relations:
        recipe = session.query(Recipes).filter_by(recipe_id=relation.recipe_id).first()
        element = session.query(Elements).filter_by(element_id=relation.element_id).first()
        if recipe and element:
            print(f"Recipe: {recipe.recipe_name} - Element: {element.element_name}")

if __name__ == "__main__":
    list_relations()
