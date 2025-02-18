from http.client import HTTPException

from fastapi import FastAPI
import pyodbc

from pythonProject.custormer.config import settings

app = FastAPI()

def get_connection():
    return pyodbc.connect(settings.SQLALCHEMY_DATABASE_URL)

@app.get("/items/")
async def read_items():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT * FROM Users')  # Thay your_table_name bằng tên bảng
        rows = cursor.fetchall()
        return {"data": [dict(zip([column[0] for column in cursor.description], row)) for row in rows]}
    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail="Error executing query")
    finally:
        cursor.close()
        conn.close()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
