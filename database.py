from sqlmodel import Session, create_engine
from config import DATABASE_URL

# Conexión a MySQL con pymysql
SQLALCHEMY_DATABASE_URL = DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Dependency para usar en los endpoints
def get_db():
    with Session(engine) as session:
        yield session