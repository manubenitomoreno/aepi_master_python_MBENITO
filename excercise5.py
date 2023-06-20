"""
a.	Quieres hacer un creador de recetas de ensaladas sencillo y minimalista. 
  i.	Decides guardar en SQL las recetas y los ingredientes.
  ii.	A cada receta corresponden 1 o más ingredientes.
  iii.	Dispones de 20 ingredientes diferentes y creas 5 recetas.
b.	Quieres hacer un informe en CSV de tus recetas.
  i.	Generas un informe donde aparezca una fila cada vez que un ingrediente aparece en una receta indicando sea el ingrediente que el nombre de la receta.
c.	Quieres recopilar información sobre un artículo de la Wikipedia de tu elección.
  i.	Del cuerpo del artículo:
    1.	¿Cuántas palabras tienen más de 4 caracteres?
    2.	¿Cuáles son las 5 palabras más repetidas?
"""
#Crear esquema, Inicializar 
#Consultar dato (recetas o ingredientes)
#Introducir dato (recetas o ingredientes)




#CREAR ESQUEMA. TABLA ELEMENTOS (DRESSINGS E INGREDIENTES) + TABLA RECETAS
  #TABLA ELEMENTOS: element_id, element_type (ingredient y dressing), element_name
  #TABLA RECETAS: recipe_id, recipe_name, ARRAY(recipe_elements)
  #TABLA RELACIONES: many2many UNA FILA POR CADA RELACION ELEMENTO-RECETA
#RELACIONAR ELEMENTOS CON RECETAS
#INPUT DATA ELEMENTOS

#INPUT DATA NUEVA RECETA (ingredientes para la receta)
  #SI EL INGREDIENTE YA EXISTE, AVISAR
  #SI NO EXISTE, PROMPTEAR INGREDIENTE
  
#OUTPUT DATA QUERY SOBRE ELEMENTOS AGRUPANDO POR RECETAS
#TRANSFORMAR A CSV

#TABLA ELEMENTOS
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
  'potato'
]
input_dressings = [
  'cesar',
  'vinagrette',
  'mediterranean',
  'asian']  
#TABLA RECETAS
input_recetas = ['mediterranean salad','cesar salad','asian salad','potato salad','garden salad']
#TABLA RELACIONES 

input_relations = {'mediterranean salad':['lettuce','tomato','olives','cucumber'],'cesar salad':['lettuce','chicken','breadcrums'],'asian salad':[],'potato salad':[],'garden salad':[]}

pat

"""
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///my_recipes.db', echo=True)
Base = declarative_base()


class Recipes(Base):

    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String)  


    def __init__(self, name):

        self.name = name    

class Elements(Base):

    __tablename__ = "elements"

    element_id = Column(Integer, primary_key=True)
    element_name = Column(String)
    element_type = Column(String)  


    def __init__(self, name):

        self.name = name    
        

class Relations(Base):

    __tablename__ = "relations"

    relation_id = Column(Integer, primary_key=True)
    element_id = Column(String)
    recipe_id = Column(String)  

    def __init__(self, name):

        self.name = name    


Base.metadata.create_all(engine)

"""