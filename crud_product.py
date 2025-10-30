from sqlalchemy.orm import Session
import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    new_product = models.Product(name=product.name,price=product.price,description=product.description,owner_id=product.owner_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_products(db: Session):
    return db.query(models.Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None
    db_product.name=product.name
    db_product.price=product.price
    db_product.description=product.description
    db_product.owner_id=product.owner_id
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None
    
    db.delete(db_product)
    db.commit()
    return db_product

   