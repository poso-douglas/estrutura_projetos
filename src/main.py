from fastapi import FastAPI

app = FastAPI()

data = [{
    "id":1,
    "produto":"notebook",
    "descricao":"notebook Azus",
    "preco":100
    },
    {
    "id":2,
    "produto":"cellphone",
    "descricao":"cellphone Samsung",
    "preco":1500
    },
    {
    "id":3,
    "produto":"mouse",
    "descricao":"optical mouse",
    "preco":47
    }
]

@app.get("/")
def root_path():
    return {"name":"Poso"}

@app.get("/product/{id}")
def product_from_id(id:int):
    for product in data:
        if product["id"] == id:
            return product