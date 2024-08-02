from ..app.functions import product_from_id, create_product,data
import pytest

def test_product_from_id():
    # Test existing product
    assert product_from_id(1) == {
        "id": 1,
        "produto": "notebook",
        "descricao": "notebook Azus",
        "preco": 100
    }

    # Test non-existing product
    assert product_from_id(99) == {}

def test_create_product():
    new_product = {
        "id": 4,
        "produto": "keyboard",
        "descricao": "wireless keyboard",
        "preco": 60
    }

    # Add the new product
    create_product(new_product)

    # Check if the product was added to the data list
    assert new_product in data

if __name__ == "__main__":
    pytest.main()
