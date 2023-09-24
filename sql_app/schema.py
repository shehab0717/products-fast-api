from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    img_url: str

class ProductIn(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

class CategoryIn(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

class Category(CategoryBase):
    id: int
    products: list[ProductOut] = []

class Product(ProductBase):
    id: int
    category_id: int