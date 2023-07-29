from db_models import MongoDBInterface
from db_aggregate import stats_collection

if __name__ == '__main__':
    interactor = MongoDBInterface('tienda', 'productos')
    interactor.populate_random_collection(1000)
    # Call the necessary aggregation functions and provide the 'group_by' parameter if needed
    stats_collection(interactor, 'tipo')
    stats_collection(interactor)

    interactor.close_connection()
