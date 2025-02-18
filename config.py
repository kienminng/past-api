import os

class Settings:
    SQLALCHEMY_DATABASE_URL = (
        f"data source={os.getenv('DB_SERVER')};initial catalog={os.getenv('DB_NAME')}; persist security info=true ;User ID={os.getenv('DB_USER')};Password={os.getenv('DB_PASSWORD')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

settings = Settings()