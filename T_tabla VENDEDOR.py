import pandas as pd
# Concatenar las columnas 'apellido_vendedor' y 'nombre_vendedor' directamente en 'vendedor'
dataset = dataset.assign(
    vendedor=dataset['apellido_vendedor'] + ', ' + dataset['nombre_vendedor']
).drop(columns=['apellido_vendedor', 'nombre_vendedor'])

# Eliminar filas donde todas las columnas tienen valores nulos, en caso exista
dataset.dropna(how='all', inplace=True)

# Reordenar las columnas
dataset = dataset[['cod_vendedor', 'vendedor', 'supervisor']]

