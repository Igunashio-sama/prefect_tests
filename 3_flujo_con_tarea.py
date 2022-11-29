import requests
from prefect import flow, task

@task
def tarea_llama_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@flow
def flujo(url):
    respuesta = tarea_llama_api(url)
    return respuesta

print(flujo("https://jsonplaceholder.typicode.com/users"))