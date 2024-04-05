from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as student_router

config = dotenv_values(".env")

app = FastAPI()

# Initialize MongoDB client and database during startup
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

app.include_router(student_router, tags=["students"], prefix="/student")