from config import settings
import  pyodbc

def check_connection():
    try:

        with pyodbc.connect(settings.SQLALCHEMY_DATABASE_URL) as connection:
            print("Kết nối thành công!")
    except Exception as e:
        print("Lỗi khi kết nối:", e)

if __name__ == "__main__":
    check_connection()