""" import requests

url = 'https://official-joke-api.appspot.com/jokes/ten?id=220'
response = requests.get(url)

if response.status_code == 200:
    jokes = response.json()
    
    for joke in jokes:
        print(joke['setup'])
        print(joke['punchline'], end='\n\n')
else:
    print(f"Произошла ошибка при выполнении запроса. Код ошибки: {response.status_code}") """