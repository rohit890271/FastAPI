from fastapi import FastAPI
from database import engine
import models
from routers import users , products,JWT_Auth
from dotenv import load_dotenv
load_dotenv()



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router)
app.include_router(products.router)
#app.include_router(auth.router)
app.include_router(JWT_Auth.router)

