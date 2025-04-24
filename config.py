# Configuración de la base de datos
DATABASE_CONFIG = {
    "USER": "root",
    "PASSWORD": "",
    "HOST": "localhost",
    "DATABASE": "examplekanban"
}

# URL de conexión
DATABASE_URL = f"mysql+pymysql://{DATABASE_CONFIG['USER']}:{DATABASE_CONFIG['PASSWORD']}@{DATABASE_CONFIG['HOST']}/{DATABASE_CONFIG['DATABASE']}"