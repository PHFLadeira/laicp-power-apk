import requests

apiKey = "7f86f90fa68746dd7eae70b7bd18c36f"  # Sua chave API real
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

cityName = 'Manaus'

completeURL = baseURL + cityName + '&appid=' + apiKey

response = requests.get(completeURL)
data = response.json()

# Verifique o código de status da resposta
if data["cod"] != "404":
    temperatura_k = data["main"]["temp"]
    umidade = data["main"]["humidity"]
    temperatura_fahrenheit = (temperatura_k - 273.15) * 9/5 + 32  # Convertendo para Fahrenheit
    ###print(f"A temperatura em {cityName} é {temperatura_fahrenheit:.2f}°F")
#else:
    #print("City Not Found!")