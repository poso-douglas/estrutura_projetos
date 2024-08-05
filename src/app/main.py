from typing import List
from fastapi import FastAPI, HTTPException, APIRouter
from ..models.model import ProductSchema
from .functions import data, create_product, product_from_id
from ..connections.database import session,Products, engine
from sqlalchemy.orm import Session

ses = Session(bind=engine)

app = FastAPI()

@app.get("/")
def root_path():
    return {"name":"Poso"}

@app.get("/produtos", response_model=List[ProductSchema])
def get_products():
    prd = ses.query(Products).all()
    return prd


@app.get("/product/{id}",response_model=List[ProductSchema])
def get_product_id(id:int):
    product_id = ses.query(Products).filter(Products.id == id)
    print(type(product_id))
    if product_id == {}:
        raise HTTPException(status_code=404, detail=f"Item {id} not found") 
    else:
        return product_id
    
@app.post("/product", response_model=ProductSchema)
def insert_product(prd:ProductSchema):
    prd = Products(id=prd.id,produto=prd.produto,descricao=prd.descricao,preco=prd.preco)
    ses.add(prd)
    ses.commit()
    ses.refresh(prd)
    return prd

    