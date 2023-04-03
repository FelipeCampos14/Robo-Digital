from models.base import Base
from sqlalchemy import Column, Integer, String

# Criando a classe com o nome da tabela, as chaves e suas respectivas tipagens
class Coordenada(Base):
    __tablename__ = "Coordenada"
    id = Column(Integer, primary_key = True)
    x_db = Column(String)
    y_db = Column(String)
    z_db = Column(String)

    def __repr__(self) -> str:
        return f"Coordenada(id={self.id}, x ={self.x_db}, y ={self.y_db}, z ={self.z_db})"