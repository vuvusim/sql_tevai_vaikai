from modelis import engine, Tevas, Vaikas
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()




def create_tevas(vardas, pavarde):
    tevas = Tevas(vardas=vardas, pavarde=pavarde)
    session.add(tevas)
    session.commit()
    return tevas

def read_tevai():
    tevai = session.query(Tevas).all()
    return tevai

def update_tevas(tevas_id, **kwargs):
    tevas = session.query(Tevas).get(tevas_id)
    if tevas:
        if "vardas" in kwargs:
            tevas.vardas = kwargs["vardas"]
        if "pavarde" in kwargs:
            tevas.pavarde = kwargs["pavarde"]
        session.commit()
    else:
        print(f"KLAIDA: Tevas su ID: {tevas_id} neegzistuoja")

def delete_tevas(tevas_id):
    tevas = session.query(Tevas).get(tevas_id)
    if tevas:
        session.delete(tevas)
        session.commit()
        return True
    else:
        print(f"KLAIDA: Tevas su ID: {tevas_id} neegzistuoja")

def create_vaikas(vardas, pavarde, tevas, mokymo_istaiga=None):
    vaikas = Vaikas(vardas=vardas, pavarde=pavarde, tevas=tevas, mokymo_istaiga=mokymo_istaiga)
    session.add(vaikas)
    session.commit()
    return vaikas

def read_vaikai():
    return session.query(Vaikas).all()

# programa skirta testavimui
if __name__ == "__main__":
    # Naujas Tevas
    # naujas_tevas = create_tevas("Simas", "Venskus")
    # print(naujas_tevas.id, naujas_tevas.vardas, naujas_tevas.pavarde)
    # update_tevas(1, vardas="Geras", pavarde="Programuotojas")
    # update_tevas(1, vardas="Neblogas")
    # print(delete_tevas(1))
    # tevas = session.query(Tevas).get(1)
    # naujas_vaikas = create_vaikas("Deimante", "Povilaityte", tevas, "Papiles Gimnazija")
    print(read_vaikai())
    