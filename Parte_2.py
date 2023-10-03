import numpy as np
import pandas as pd

# Suponiendo que 'data' contiene el dataset y 'age' es la columna de edades
ages_list = data["age"]
ages_np = np.array(ages_list)

# Convertir a DataFrame
df = pd.DataFrame(data)

# Separar en dos DataFrames
df_perecieron = df[df["is_dead"] == 1]
df_sobrevivieron = df[df["is_dead"] == 0]

# Calcular promedio de edades
average_age_perecieron = np.mean(df_perecieron["age"].to_numpy())
average_age_sobrevivieron = np.mean(df_sobrevivieron["age"].to_numpy())

print(f"Promedio de edades de personas que perecieron: {average_age_perecieron} años")
print(f"Promedio de edades de personas que sobrevivieron: {average_age_sobrevivieron} años")
