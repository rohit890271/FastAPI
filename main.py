from fastapi import FastAPI
from database import engine
import models
from routers import users , products,auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)

