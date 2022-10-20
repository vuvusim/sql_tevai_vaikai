from bankas_crud import *

while True:
    print("Pasirinkite")
    print("1: Ivesti asmeni")
    print("2: Iveskite banka")
    print("3: Prideti saskaita")
    print("4: Saskaitos balansas")
    print("5: Perziureti Asmenis, Bankus arba Saskaitas")
    print("0: Iseiti")
    pasirinkimas = int(input().casefold())
    if pasirinkimas == 1:
        sukurti_asmeni()
    elif pasirinkimas == 2:
        sukurti_banka()
    elif pasirinkimas == 3:
        sukurti_sask()
    elif pasirinkimas == 4:
        balansas()
    elif pasirinkimas == 5:
        rodyti_asmenys_bankai_sask()
    else:
        pasirinkimas = 0
        break

