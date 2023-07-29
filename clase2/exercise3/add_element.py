from db import session
from models import Elements

def add_element():
    
    element_name = input("Enter the element name: ")
    
    existing_element = session.query(Elements).filter_by(element_name=element_name).first()
    
    if existing_element:
        print(f"Element {element_name} already exists in the database.")
        return
    
    element_type = input("Enter the element type: (ingredient or dressing)")
    
    #Enforcing the expected values in the column element_type
    while True:
        
        similar_elements = session.query(Elements).filter_by(element_type=element_type).all()
        for elem in similar_elements:
            if elem.element_name.lower() == element_name.lower():
                print(f"Similar element {elem} already exists in the database.")
                return
            
        element_type = input("Enter the element type: (ingredient or dressing)")
        if element_type in ["dressing", "ingredient"]:
            break
        else:
            print("Invalid element type. Please enter either 'dressing' or 'ingredient'.")

    new_element = Elements(element_name=element_name, element_type=element_type)

    session.add(new_element)
    session.commit()

    print("Element added successfully")
    
if __name__ == '__main__':
    add_element()
    #run()
