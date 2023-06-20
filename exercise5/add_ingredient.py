from db import *
from models import Elements


def add_element():
    element = Elements(
        input("Please enter the name of the element"),
        input("Please enter the kind of element (ingredient or dressing)"))
    db.session.add(element)
    print(element.id)
    agua = Producto('Agua', 0.3)
    db.session.add(agua)
    db.session.commit()
    print(arroz.id)


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()
