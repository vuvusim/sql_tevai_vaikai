
from bankas_model import Asmuo, Bankas, Saskaita, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()




def sukurti_asmeni():
    print("--- Naujas Darbuotojas ---")
    try:
        vardas = input("Vardas: ")
        pavarde = input("Pavarde: ")
        asmens_kodas = int(input("Asmens kodas: "))
        tel_nr = input("Telefono numeris: ")
    except ValueError:
        print("KLAIDA: Neteisinga ivestis")
        return
    else:
        asmuo = Asmuo(vardas, pavarde, asmens_kodas, tel_nr)
        session.add(asmuo)
        session.commit()

def sukurti_banka():
    print("--- Naujas Bankas ---")
    try:
        pavadinimas = input("Iveskite banko pavadinima: ")
        adresas = input("Iveskite banko daresa: ")
        banko_kodas = int(input("Iveskite banko koda: "))
        swift_kodas = input("Iveskite SWIFT koda: ")
    except ValueError:
        print("KLAIDA: Neteisinga ivestis")
        return
    else:
        bankas = Bankas(pavadinimas, adresas, banko_kodas, swift_kodas)
        session.add(bankas)
        session.commit()

def asmuo_bankas():
    print("--- Asmenys ---")
    vartotojai = session.query(Asmuo).all()
    for vartotojas in vartotojai:
        print(vartotojas)
    print("--- Bankai ---")
    bankai = session.query(Bankas).all()
    for bankas in bankai:
        print(bankas)
    
def sukurti_sask():
    print("--- Nauja Saskaita ---")
    asmuo_bankas()
    vartotojas_id = int(input("Pasirinkite asmens ID: "))
    banko_id = int(input("Iveskite banko ID: "))
    numeris = input("Iveskite saskaitos numeri: ")
    balansas = 0
    saskaita = Saskaita(numeris=numeris, balansas=balansas, asmuo_id=vartotojas_id, bankas_id=banko_id)
    session.add(saskaita)
    session.commit()

def balansas():
    print("--- Saskaitos balansas ---")
    saskaitos = session.query(Saskaita).all()
    for saskaita in saskaitos:
        print(saskaita)
    saskaitos_id = int(input("Pasirinkite saskaitos ID: "))
    pasirink_sask = session.query(Saskaita).get(saskaitos_id)
    ivedimas = float(input("Iveskite saskaitos pajamas arba islaidas: "))
    pasirink_sask.balansas += ivedimas
    session.commit()

def rodyti_asmenys_bankai_sask():
    print("--- Perziureti Asmenis, Bankus, Saskaitas ---")
    print("1: Asmenys")
    print("2: Bankai")
    print("3: Saskaitos")
    pasirinkimas = int(input("Pasirinkite veiksma: "))
    if pasirinkimas == 1:
        asmenys = session.query(Asmuo).all()
        for asmuo in asmenys:
            print(asmuo)
    elif pasirinkimas == 2:
        bankai = session.query(Bankas).all()
        for bankas in bankai:
            print(bankas)
    elif pasirinkimas == 3:
        saskaitos = session.query(Saskaita).all()
        for saskaita in saskaitos:
            print(saskaita)



