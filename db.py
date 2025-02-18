from config import settings
import  pyodbc

def check_connection():
    try:
        # Kết nối tới SQL Server
        connection = pyodbc.connect(settings.SQLALCHEMY_DATABASE_URL)
        print("Kết nối thành công!")

        # Thực thi một câu truy vấn đơn giản (ví dụ: kiểm tra phiên bản SQL Server)
        cursor = connection.cursor()
        cursor.execute("SELECT @@version;")
        result = cursor.fetchone()
        print("Phiên bản SQL Server:", result[0])

        cursor.close()  # Đảm bảo đóng cursor khi không còn sử dụng
        connection.close()  # Đảm bảo đóng kết nối khi không còn sử dụng
    except Exception as e:
        print("Lỗi khi kết nối:", e)

if __name__ == "__main__":
    check_connection()