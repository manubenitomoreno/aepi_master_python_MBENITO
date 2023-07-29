import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Recipes(db.Base):

    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String)
    #TODO created_on, created_by    


    def __init__(self, recipe_name):

        self.recipe_name = recipe_name    

class Elements(db.Base):

    __tablename__ = "elements"

    element_id = Column(Integer, primary_key=True, autoincrement=True)
    element_name = Column(String)
    element_type = Column(String)
    #TODO created_on, created_by    


    def __init__(self, element_name, element_type):

        self.element_name = element_name    
        self.element_type = element_type    
        
        
class Relations(db.Base):
    __tablename__ = "relations"

    relation_id = Column(Integer, primary_key=True)
    element_id = Column(Integer, ForeignKey("elements.element_id"))
    recipe_id = Column(Integer, ForeignKey("recipes.recipe_id"))

    def __init__(self, element_id, recipe_id):
        self.element_id = element_id
        self.recipe_id = recipe_id
        
