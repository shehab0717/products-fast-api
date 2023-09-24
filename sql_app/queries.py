from sqlalchemy.orm import Session, joinedload
from sql_app import models
from sql_app import schema
from sqlalchemy import update


def create_category(db: Session, category_in: schema.CategoryIn):
    print(category_in)
    category = models.Category(name=category_in.name)
    print(category)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_categories(db: Session):
    return db.query(models.Category).all()
    


def get_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    print(product)
    return product

def get_products(db: Session, category_id: int | None):
    if category_id is None:
        return db.query(models.Product).all()
    return get_category_products(db, category_id=category_id)


def create_product(db: Session, product_in: schema.ProductIn, category_id: int):
    product = models.Product(**product_in.model_dump(), category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_category_products(db: Session, category_id: int):
    return db.query(models.Product).filter(models.Product.category.has(id=category_id)).all()


def update_product(db: Session, product_id: int, updated_product: schema.ProductIn):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product is None:
        return None
    product.name = updated_product.name
    product.price = updated_product.price
    product.quantity = updated_product.quantity
    product.img_url = updated_product.img_url
    db.commit()
    return product

    
