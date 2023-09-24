from fastapi import FastAPI, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session
from sql_app.main import SessionLocal, engine
from sql_app import schema
from sql_app import queries
from sql_app import models
from typing import Annotated

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/categories", response_model=list[schema.CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return queries.get_categories(db)

@app.post("/categories", response_model=schema.Category)
def add_category(category_in: schema.CategoryIn, db: Session = Depends(get_db)):
    return queries.create_category(db, category_in)


@app.post("/category/{category_id}/products", response_model=schema.Product)
def add_product(category_id: int, product_in: schema.ProductIn, db: Session = Depends(get_db)):
    cat = queries.get_category(db, category_id=category_id)
    if cat is None:
        raise HTTPException(404, f"Can't find category with id: {category_id}")
    return queries.create_product(db, product_in=product_in,category_id=category_id)


@app.get("/category/{category_id}", response_model=schema.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return queries.get_category(db, category_id=category_id)



@app.get("/products")
def get_products(category_id: Annotated[int, Query(alias="categoryID")], db:Session = Depends(get_db)):
        return queries.get_products(db, category_id=category_id)


@app.get("/product/{product_id}")
def get_product(product_id: int, db:Session = Depends(get_db)):
    product = queries.get_product(db, product_id=product_id)
    if product is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Product with id: {product_id} isn't found")
    return product


@app.put("/product/{product_id}", response_model=schema.Product)
def update_product(product_id: int, updated_product: schema.ProductIn, db: Session = Depends(get_db)):
    p = queries.update_product(db, product_id=product_id, updated_product= updated_product)
    if p is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Product with id: {product_id} isn't found")
    return p



