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


def delete_object(object_class, object_id):
    obj = session.query(object_class).get(object_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    else:
        print(f"KLAIDA: {object_class.__name__} su ID: {object_id} neegzistuoja")

def update_object(object_class, object_id, **kwargs):
    obj = session.query(object_class).get(object_id)
    if obj and kwargs:
        for column_name, value in kwargs.items():
            if hasattr(obj, column_name):
                setattr(obj, column_name, value)
            else:
                print(f"KLAIDA: {obj} neturi {column_name} atributo")
        else:
            session.commit()
            return obj
    else:
        print(f"KLAIDA: {object_class.__name__} su ID: {object_id} neegzistuoja")

def create_vaikas(vardas, pavarde, tevas, mokymo_istaiga=None):
    vaikas = Vaikas(vardas=vardas, pavarde=pavarde, tevas=tevas, mokymo_istaiga=mokymo_istaiga)
    session.add(vaikas)
    session.commit()
    return vaikas

def read_vaikai():
    return session.query(Vaikas).all()

# programa skirta testavimui
if __name__ == "__main__":
    vaikas = session.query(Vaikas).filter(Vaikas.pavarde.ilike("Po%")).first()
    tevas = session.query(Tevas).filter(Tevas.pavarde.ilike("Ven%")).first()
    ivaikintas = update_object(Vaikas, vaikas.id, tevas=tevas, vardas="Ivaikintas")
    print("Python objektas ivaikintas:\n", ivaikintas)
    print("Perkraunam is duomenu bazes:\n", read_vaikai())

    # naujas_tevas = create_tevas("Niekam", "Tikes")
    # naujas_vaikas = create_vaikas("Vaikas", "Vargselis", naujas_tevas)
    # print(read_vaikai())
    # delete_object(Tevas, naujas_tevas.id)
    # print(read_vaikai())

    # Naujas Tevas
    # naujas_tevas = create_tevas("Simas", "Venskus")
    # print(naujas_tevas.id, naujas_tevas.vardas, naujas_tevas.pavarde)

    # update_tevas(1, vardas="Geras", pavarde="Programuotojas")
    # update_tevas(1, vardas="Neblogas")
    # print(delete_tevas(1))

    # tevas = session.query(Tevas).get(1)
    # naujas_vaikas = create_vaikas("Deimante", "Povilaityte", tevas, "Papiles Gimnazija")
    