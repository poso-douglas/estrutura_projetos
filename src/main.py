from fastapi import FastAPI, HTTPException
from .model import ProductSchema
from .functions import data, create_product, product_from_id

app = FastAPI()

@app.get("/")
def root_path():
    return {"name":"Poso"}

@app.get("/product/{id}",response_model=ProductSchema)
def get_product_id(id:int):
    product_id = product_from_id(id)
    if product_id == {}:
        raise HTTPException(status_code=404, detail=f"Item {id} not found") 
    else:
        return product_id
    
@app.post("/product", response_model=ProductSchema)
def insert_product(prd:ProductSchema):
    return create_product(prd)
    