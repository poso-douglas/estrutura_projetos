
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


def product_from_id(id:int):
    """
        Captura um produto especifico passando o seu ID
    """
    for product in data:
        if product["id"] == id:
            return product   
    return {}



def create_product(prd:dict):
    data.append(prd)
    return prd