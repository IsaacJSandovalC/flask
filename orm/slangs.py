from sqlalchemy import Column, String, Integer
from conexion import Base

class Slangs(Base):
    __tablename__ = 'Slangs'

    slangs = {
        1: {"palabra": "que xopa", "significado": "expresión utilizada para saludar"},
        2: {"palabra": "yalabetia", "significado": "accion y efecto de sorpresa"},
        3: {"palabra": "chantin", "significado": "referencia al domicilio de alguna persona"},
        4: {"palabra": "fren", "significado": "haciendo referencia a algun amigo o conocido"},
        5: {"palabra": "lapesillo", "significado": "haciendo referencia a que la persona es un joven"}
    }
  
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    definicion = Column(String(255))

    def __init__(self, nombre, definicion):
        self.nombre = nombre
        self.definicion = definicion

    @classmethod
    def insert_slangs(cls, session):
        for key, value in cls.slangs.items():
            slang = session.query(cls).filter(cls.nombre == value['palabra']).first()
            if slang:
                slang.significado = value['significado']
            else:
                slang = cls(nombre=value['palabra'], definicion=value['significado'])
                session.add(slang)
        session.commit()








