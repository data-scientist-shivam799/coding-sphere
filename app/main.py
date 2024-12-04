from mongoengine import connect
from fastapi import FastAPI
from app.routes import auth_routes, project_routes

app = FastAPI()

connect("api_db", host="localhost", port=27017)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(project_routes.router)