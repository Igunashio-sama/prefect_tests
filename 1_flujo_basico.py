from prefect import flow

@flow
def flujo():
    print("Ejecutando mi primer flujo")
    return "Adios"

print(flujo())