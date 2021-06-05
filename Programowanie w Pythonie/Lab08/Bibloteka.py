from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()


class Biblioteka():
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.engine = create_engine(f'sqlite:///{self.nazwa}.db', echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def Dodaj_Uzytkownika(self, czytelnik):
        self.session.add(czytelnik)
        self.session.commit()

    def Dodaj_Ksiazke(self, ksiazka):
        self.session.add(ksiazka)
        self.session.commit()

    def Wypozycz(self, id_uczestnika, id_ksiazki):
        klient = self.session.query(Czytelnik).filter(Czytelnik.id == id_uczestnika).first()
        if not klient:
            return "Nie ma czytelnika o takim id"
        ksiazka = self.session.query(Ksiazka).filter(Ksiazka.id_ksiazki == id_ksiazki).first()
        if not ksiazka:
            return "Nie ma ksiazki o takim id"
        if ksiazka.Wypozyczona:
            return "Ta ksiazka jest juz wyporzyczona"
        ksiazka.Wypozyczona = True
        a = Wypozycz(id_uczestnika, id_ksiazki)
        self.session.add(a)
        self.session.commit()
        return "git"


class Czytelnik(Base):
    __tablename__ = 'Czytelnicy'
    id = Column(Integer, primary_key=True)
    imie = Column(String)
    nazwisko = Column(String)
    psel = Column(Integer)

    def __init__(self, Imie, Nazwisko, Pesel):
        self.imie = Imie
        self.nazwisko = Nazwisko
        self.psel = Pesel


class Ksiazka(Base):
    __tablename__ = 'Ksiazki'
    id_ksiazki = Column(Integer, primary_key=True)
    Tytul = Column(String)
    Autor = Column(String)
    Katergoria = Column(String)
    Wypozyczona = Column(Boolean)

    def __init__(self, Tytul, Autor, Kategoria):
        self.Tytul = Tytul
        self.Autor = Autor
        self.Katergoria = Kategoria
        self.Wypozyczona = False


class Wypozycz(Base):
    __tablename__ = "Wypozyczenia"
    id = Column(Integer, primary_key=True)
    idCzytelnika = Column(Integer, ForeignKey("Czytelnicy.id"))
    idKsiazki = Column(Integer, ForeignKey("Ksiazki.id_ksiazki"))
    oddane = Column(Boolean)

    def __init__(self, id1, id2):
        self.idCzytelnika = id1
        self.idKsiazki = id2
        self.oddane = False


if __name__ == "__main__":
    Narodowa = Biblioteka("Narodowa")
    bob = Czytelnik("Marek", "Marlej", 112)
    Narodowa.Dodaj_Uzytkownika(bob)
    tytanik = Ksiazka("Tytanik", "Ja sam", "Komedia")
    Narodowa.Dodaj_Ksiazke(tytanik)
    print(Narodowa.Wypozycz(1, 1))
