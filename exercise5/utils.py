from sqlalchemy import insert, select, create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_recipes.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

def add_elements(Table,values_dict):
    for Table(values)
    session.add(arroz)
    print(arroz.id)
    
    
    session.commit()
    
    
