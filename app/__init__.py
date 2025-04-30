# from flask import Flask
from fastapi import FastAPI
# from app.extensions import db,limiter,redis_client
# from app.config import Config
# from app.database import init_db

def create_app():
    app = FastAPI()
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/test"

    # app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    # migrate.init_app(app, db)
    # jwt.init_app(app)
    limiter.init_app(app)
    
    # Configure Redis
    
    # Configure Celery
    # celery.conf.update(app.config)

    # Initialize database with retry mechanism

    
    return app