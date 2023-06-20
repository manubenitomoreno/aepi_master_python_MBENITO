from db import *

class Recipes(Base):

    __tablename__ = "recipes"

    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String)
    #TODO created_on, created_by    


    def __init__(self, name):

        self.name = name    

class Elements(Base):

    __tablename__ = "elements"

    element_id = Column(Integer, primary_key=True)
    element_name = Column(String)
    element_type = Column(String)
    #TODO created_on, created_by    


    def __init__(self, name):

        self.name = name    
        

class Relations(Base):

    __tablename__ = "relations"

    relation_id = Column(Integer, primary_key=True)
    element_id = Column(String, ForeignKey("elements.element_id"))
    recipe_id = Column(String, ForeignKey("recipes.recipe_id"))
    #TODO created_on, created_by  

    def __init__(self, name):

        self.name = name 