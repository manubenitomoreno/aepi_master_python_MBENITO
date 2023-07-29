from db_models import * 

def stats_collection(interactor: MongoDBInterface, group_by: str = None):
    if group_by:
        # Realizar resumen por cada clase en el campo 'tipo'
        pipeline = [
            {
                '$group': {
                    '_id': '$' + group_by,
                    'total': {'$sum': '$precio'},
                    'average': {'$avg': '$precio'}
                }
            }
        ]
        result = list(interactor.collection.aggregate(pipeline))

        if result:
            print(f"Resumen por '{group_by}':")
            for doc in result:
                campo = doc['_id']
                total = doc['total']
                promedio = doc['average']
                print(f"{campo}: Total: {total}, Promedio: {promedio}")
        else:
            print(f"No se encontraron resultados para el campo '{group_by}'.")
    else:
        # Recopilar estadísticas totales
        pipeline_sum = [
            {
                '$group': {
                    '_id': None,
                    'total': {'$sum': '$precio'}
                }
            }
        ]
        result_sum = list(interactor.collection.aggregate(pipeline_sum))
        if result_sum:
            sum_prices = result_sum[0]['total']
            print(f"Suma de los precios totales: {sum_prices}")
        else:
            print("No se encontraron resultados para la suma de precios totales.")

        pipeline_avg = [
            {
                '$group': {
                    '_id': None,
                    'average': {'$avg': '$precio'}
                }
            }
        ]
        result_avg = list(interactor.collection.aggregate(pipeline_avg))
        if result_avg:
            avg_price = result_avg[0]['average']
            print(f"Promedio de los precios totales: {avg_price}")
        else:
            print("No se encontraron resultados para el promedio de precios totales.")

        if result_sum and result_avg:
            value_estimation = sum_prices * avg_price
            print(f"Valor estimado del stock total: {value_estimation}")
        else:
            print("No se pueden calcular resultados para la estimación del valor del stock total.")

