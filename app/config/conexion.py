from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()  # Cargar variables de entorno desde el archivo .env

conexion = create_engine(f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_SERVER')}")

try:
    # Probar la conexión
    with conexion.connect() as conn:
        print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    