import dask.dataframe as dd
from dask.distributed import Client

# Conectar al scheduler de Dask
client = Client('tcp://dask-scheduler:8786')  # Asegúrate de usar la dirección correcta del scheduler

# Cargar los datos de MovieLens
df = dd.read_csv('/data/ml-100k/u.data', sep='\t', names=["user_id", "item_id", "rating", "timestamp"])

# Realizar alguna operación distribuida
mean_ratings = df.groupby('item_id')['rating'].mean().compute()

# Mostrar las medias de las calificaciones por item_id
print(mean_ratings)
