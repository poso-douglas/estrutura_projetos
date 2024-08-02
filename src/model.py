from pydantic import BaseModel, PositiveInt,PositiveFloat


class ProductSchema(BaseModel):
    id: PositiveInt
    produto: str
    descricao: str
    preco: PositiveFloat
    