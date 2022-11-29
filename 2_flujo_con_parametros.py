import requests
from prefect import flow


@flow
def flujo_con_parametros(url):
    return requests.get(url).json()


resultado = flujo_con_parametros("https://jsonplaceholder.typicode.com/users")

print(resultado)