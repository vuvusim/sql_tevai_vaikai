from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///data/saskaitos.db")
Base = declarative_base()

class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asmens_kodas = Column("asmens_kodas", Integer, unique=True)
    tel_nr = Column("tel_nr", Integer)

    def __init__(self, vardas, pavarde, asmens_kodas, tel_nr):
        self.vardas = vardas
        self.pavarde = pavarde
        self.asmens_kodas = asmens_kodas
        self.tel_nr = tel_nr

    def __repr__(self):
        return f"{self.id}, {self.vardas} {self.pavarde}, {self.asmens_kodas}, {self.tel_nr}"


class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    adresas = Column("adresas", String)
    banko_kodas = Column("banko_kodas", Integer)
    swift_kodas = Column("SWIFT_kodas", String)

    def __init__(self, pavadinimas, adresas, banko_kodas, swift_kodas):
        self.pavadinimas = pavadinimas
        self.adresas = adresas
        self.banko_kodas = banko_kodas
        self.swift_kodas = swift_kodas
    
    def __repr__(self):
        return f"{self.id}, {self.pavadinimas}, {self.adresas}, {self.banko_kodas}, {self.swift_kodas}"


class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key=True)
    numeris = Column("numeris", String)
    balansas = Column("balansas", Float)
    asmuo_id = Column("asmens_id", Integer, ForeignKey("asmuo.id"))
    asmuo = relationship("Asmuo")
    bankas_id = Column("banko_id", Integer, ForeignKey("bankas.id"))
    bankas = relationship("Bankas")

    def __init__(self, numeris, balansas, asmuo_id, bankas_id):
        self.numeris = numeris
        self.balansas = balansas
        self.asmuo_id = asmuo_id
        self.bankas_id = bankas_id

    def __repr__(self):
        return f"{self.id}, {self.numeris}, {self.balansas}, {self.asmuo}, {self.bankas}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
