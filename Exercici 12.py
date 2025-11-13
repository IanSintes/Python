def majoredat(edat):
    if edat >18:
        print("Ets major d'edat, ves a treballar")
    elif edat <18:
        print("Ets menor d'edat, ves a estudiar")
    else:
        print("Tens 18 anys, disfruta!")

edat = int(input("Insereix la seva edat: "))
majoredat(edat)
edat = int(input("Insereix la seva edat: "))
majoredat(edat)