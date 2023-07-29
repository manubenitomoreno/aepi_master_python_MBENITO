from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_recipes.db', echo=True)

Base = declarative_base()
#make session 


engine = create_engine('sqlite:///almacen.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

    
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    
