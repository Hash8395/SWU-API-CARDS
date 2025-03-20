from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://swu_user:swu_password@192.168.97.2/swu_api_cards"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dépendance pour obtenir la session DB
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()