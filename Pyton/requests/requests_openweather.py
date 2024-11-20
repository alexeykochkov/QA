import requests

url = f'https://api.openweathermap.org/data/2.5/weather'
params = {"lat":54.715424, "lon":20.509207, "appid":'f7b3082e9cabd772faaded2e65cc2fb4'}
response = requests.get(url,params=params)

if response.status_code == 200:
    print(f"Запрос выполнен успешно! Ответ от сервера: {response.json()}")
else:
    print(f"Произошла ошибка при выполнении запроса. Код ошибки: {response.status_code}")