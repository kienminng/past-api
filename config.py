import os

class Settings:
    SQLALCHEMY_DATABASE_URL = (
        #f"data source={os.getenv('DB_SERVER')};initial catalog={os.getenv('DB_NAME')}; persist security info=true ;User ID={os.getenv('DB_USER')};Password={os.getenv('DB_PASSWORD')}"
        "Driver={ODBC Driver 17 for SQL Server};Server=localhost\MSSQLSERVER03;Database=training_py;Trusted_Connection=yes;"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

settings = Settings()