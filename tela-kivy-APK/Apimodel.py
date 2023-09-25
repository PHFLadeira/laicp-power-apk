from temperature import temperatura_fahrenheit, umidade  # Certifique-se de que o arquivo temperature.py esteja no mesmo diretório
import pickle
import pandas as pd

# Carregar o modelo e o scaler
with open("modelXGBoost.pkl", "rb") as f:
    modelo = pickle.load(f)

with open("scaler_x.pkl", "rb") as f:
    scaler_x = pickle.load(f)

with open("scaler_y.pkl", "rb") as f:
    scaler_y = pickle.load(f)

# Usando a variável importada como a temperatura média e a umidade média
temp_avg = temperatura_fahrenheit
hum_avg = umidade