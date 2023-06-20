from db import *
from models import * 
engine = create_engine('sqlite:///my_recipes.db', echo=True)
Base = declarative_base()  


def main():
    #TODO assert exists
    #TODO if exists warning
    print("Initializing database...")
    Base.metadata.create_all(engine)
    print("Done...")

if __name__ == "__main__":
    main()
 

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


