import csv
from db import session
from models import Relations, Recipes, Elements

def export_relations_to_csv(filename):
    relations = session.query(Relations).all()

    if not relations:
        print("No relations found.")
        return

    try:
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Recipe", "Element"])
            for relation in relations:
                recipe = session.query(Recipes).filter_by(recipe_id=relation.recipe_id).first()
                element = session.query(Elements).filter_by(element_id=relation.element_id).first()
                if recipe and element:
                    writer.writerow([recipe.recipe_name, element.element_name])
        print(f"Relations exported to {filename} successfully.")
    except Exception as e:
        print(f"Error exporting relations: {str(e)}")

if __name__ == "__main__":
    export_relations_to_csv("relations.csv")
