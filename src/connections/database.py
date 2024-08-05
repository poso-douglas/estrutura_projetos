from sqlalchemy import String,Integer, Float,Column, create_engine
from sqlalchemy.orm import  sessionmaker, declarative_base
from dotenv import load_dotenv
import os


load_dotenv()

dbuser = os.getenv("POSTGRES_DBUSER")
dbpass = os.getenv("POSTGRES_PASS")
dbport = os.getenv("POSTGRES_PORT")
dbhost = os.getenv("POSTGRES_HOST")
dbdatabase = os.getenv("POSTGRES_DATABASE")

CONNECTION_STRING = f"postgresql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbdatabase}"

engine = create_engine(CONNECTION_STRING, echo=True)
#Garante que a seção do banco será fechada
session = sessionmaker(bind=engine)

Base = declarative_base()

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, nullable=False)
    descricao = Column(String)
    preco =  Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)
