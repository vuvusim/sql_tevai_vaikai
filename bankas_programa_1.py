from bankas_model import Asmuo, Bankas, Saskaita, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

while True:
    print("Pasirinkite viena is variantu.")
    pasirinkimas = int(input("1 - iveskite vartotoja\n2 - iveskite banka\n3 - iveskite saskaita\n4 - iveskite pajamas/islaidas\n6 - perziureti vartotojus\n7 - perziureti bankus\n8 - perziureti saskaita\n9 - iseiti is programos\n"))
    if pasirinkimas == 1:
        vardas = input("Vardas: ")
        pavarde = input("Pavarde: ")
        asmens_kodas = int(input("Asmens kodas: "))
        tel_nr = int(input("Telefono numeris: "))
        asmuo = Asmuo(vardas=vardas, pavarde=pavarde, asmens_kodas=asmens_kodas, tel_nr=tel_nr)
        session.add(asmuo)
        session.commit()

    if pasirinkimas == 2:
        pavadinimas = input("Banko pavadinimas: ")
        adresas = input("Banko adresas: ")
        banko_kodas = int(input("Banko kodas: "))
        swift_kodas = input("Banko SWIFT kodas: ")
        bankas = Bankas(pavadinimas=pavadinimas, adresas=adresas, banko_kodas=banko_kodas, swift_kodas=swift_kodas)
        session.add(bankas)
        session.commit()

    if pasirinkimas == 3:
        sask_nr = input("Iveskite saskaitos numeri: ")
        balansas = 0
        vartotojai = session.query(Asmuo).all()
        for vartotojas in vartotojai:
            print(vartotojas)
        vartotojas_id = int(input("Pasirinkite vartotojo ID: "))
        bankai = session.query(Bankas).all()
        for bankas in bankai:
            print(bankas)
        banko_id = int(input("Iveskite banko ID: "))
        saskaita = Saskaita(sask_nr=sask_nr, balansas=balansas, asmuo_id=vartotojas_id, bankas_id=banko_id)
        session.add(saskaita)
        session.commit

    if pasirinkimas == 4:
        saskaitos = session.query(Saskaita).all()
        for saskaita in saskaitos:
            print(saskaita)
        saskaitos_id = int(input("Pasirinkite saskaitos ID: "))
        pasirinkta_saskaita = session.query(Saskaita).get(saskaitos_id)
        irasas = float(input("Iveskite saskaitos pajamas arba islaidas (su -)"))
        pasirinkta_saskaita.balansas += irasas
        session.commit()

    if pasirinkimas == 6:
        print(vartotojas)

    if pasirinkimas == 7:
        print(bankas)

    if pasirinkimas == 8:
        print(saskaita)

    if pasirinkimas == 9:
        quit()
