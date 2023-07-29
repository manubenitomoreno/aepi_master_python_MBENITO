from db import session, Base, engine
from models import Elements, Recipes, Relations

#DEFINE SOME BASE DATA
input_ingredients = [
  'lettuce',
  'spinach'
  'tomato',
  'carrot',
  'cucumber',
  'soybeans',
  'chicken',
  'breadcrumbs',
  'ham',
  'olives',
  'radish',
  'tuna',
  'potato']

input_dressings = [
  'cesar',
  'vinagrette',
  'mediterranean',
  'asian']  

#TABLA RECETAS
input_recetas = ['mediterranean salad','cesar salad','asian salad','potato salad','garden salad']
#TABLA RELACIONES 

input_relations = {'mediterranean salad':['lettuce','tomato','olives','cucumber'],'cesar salad':['lettuce','chicken','breadcrumbs']}



def insert_data():
    # Insert elements
    for ingredient_name in input_ingredients:
        ingredient = Elements(element_name=ingredient_name, element_type='ingredient')
        session.add(ingredient)

    for dressing_name in input_dressings:
        dressing = Elements(element_name=dressing_name, element_type='dressing')
        session.add(dressing)

    session.commit()

    # Insert recipes and relations
    for recipe_name in input_recetas:
        recipe = Recipes(recipe_name=recipe_name)
        session.add(recipe)
        session.commit()

        if recipe_name in input_relations:
            elements = input_relations[recipe_name]
            for element_name in elements:
                element = session.query(Elements).filter_by(element_name=element_name).first()
                if element:
                    relation = Relations(recipe_id=recipe.recipe_id, element_id=element.element_id)
                    session.add(relation)

    session.commit()

    print("Data inserted successfully.")

    
    
def main():
  print("Initializing database...")
  Base.metadata.create_all(engine)
  print("Inserting some initial data...")
  insert_data()
  print("Done...")

if __name__ == "__main__":
  main()
    
    
 