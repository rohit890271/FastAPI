from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas, crud_product

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db, product)

@router.get("/", response_model=list[schemas.ProductResponse])
def get_product(db: Session = Depends(get_db)):
    return crud_product.get_products(db)

@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_product.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated = crud_product.update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud_product.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": f"Products {product_id} deleted successfully"}