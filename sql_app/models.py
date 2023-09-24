from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__='category'
    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String, unique=True, index=True)
    products= relationship("Product", back_populates="category")

class Product(Base):
    __tablename__='product'
    id= Column(Integer, primary_key=True, index=True, autoincrement=True)
    name= Column(String)
    price= Column(Double)
    quantity= Column(Integer)
    img_url= Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    category= relationship("Category", back_populates="products")



