#Tehtävässä tulee tehdä kirjautumisjärjestelmä, jonka avulla voi joko kirjautua
#tai luoda uuden tunnuksen, mikäli käyttäjällä ei ole tunnusta ennestään

#Funktio sisäänkirjautumiseen
def sisaankirjautuminen():
    #Pyydetään käyttäjältä sähköposti ja salasana
    sPosti = input("Syötä sähköposti: ")
    salasana = input("Syötä salasana: ")

    #Avataan tiedosto, johon on tallennettu sähköpostit ja salasanat
    kirjautumistiedot = open("demo2_tehtava3_kayttajanimet_ja_salasanat.txt")
    #Tarkistetaan onko sähköposti ja salasana syötetty oikein
    if (f"{sPosti}:{salaus(salasana)}") in kirjautumistiedot.read():
        print("Kirjautuminen onnistui.")
    else:
        print("Sähköposti tai salasana on väärä tai käyttäjää ei ole vielä luotu")

#Funktio uuden käyttäjän luontiin
def kayttajan_luonti():
    #Pyydetään käyttäjää syöttämään sähköposti kahteen kertaan
    sPosti = input("Anna sähköposti: ")
    sPosti2 = input("Anna sähköposti uudestaan: ")
    #Jos sähköpostit täsmäävät, pyydetään salasana kaksi kertaa
    if sPosti == sPosti2 and oikeaSPosti(sPosti) == True:
        print("Salasanan täytyy olla vähintään kahdeksan merkkiä pitkä ja sisältää vähintään yksi pieni kirjain, yksi iso kirjain ja yksi numero.")
        salasana = input("Anna salasana: ")
        salasana2 = input("Anna salasana uudestaan: ")
        #Jos salasanat täsmäävät, tallennetaan käyttäjätiedot
        if salasana == salasana2 and kelvollinenSalasana(salasana) == True:
            kirjautumistiedot = open("demo2_tehtava3_kayttajanimet_ja_salasanat.txt")
            #Tarkistetaan ettei sähköposti ole jo rekisteröity
            if sPosti not in kirjautumistiedot.read():
                kirjautumistiedot = open("demo2_tehtava3_kayttajanimet_ja_salasanat.txt", "a")
                kirjautumistiedot.write(f"{sPosti}:{salaus(salasana)}\n")
            else:
                print("Kyseisellä sähköpostilla on jo olemassa käyttäjä.")
            kirjautumistiedot.close()
        else:
            print("Salasanat eivät täsmää tai salasana ei kelpaa.")
    else:
        print("Sähköpostiosoitteet eivät täsmää tai annettu sähköpostiosoite ei kelpaa.")

#Funktio, jolla salataan salasanat
def salaus(salasana: str) -> str:
    #Merkkijonot joihin on listattu kaikki sallitut merkit
    pienetKirjaimet = "abcdefghijklmnopqrstuvwxyz"
    isotKirjaimet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numerot = "0123456789"
    erikoismerkit = ".:,;-_*?+#!@$<>|/£¤%&{[]}()'"
    salattuSalasana = ""

    #Salataan salasana merkki kerrallaan ja palautetaan lopuksi salattu salasana
    for merkki in salasana:
        if merkki in pienetKirjaimet:
            salattuSalasana += pienetKirjaimet[pienetKirjaimet.find(merkki)-5].upper()
        elif merkki in isotKirjaimet:
            salattuSalasana += isotKirjaimet[isotKirjaimet.find(merkki)-7].lower()
        elif merkki in numerot:
            salattuSalasana += numerot[numerot.find(merkki)-3]
        elif merkki in erikoismerkit:
            salattuSalasana += erikoismerkit[erikoismerkit.find(merkki)-3]
    
    return salattuSalasana

#Funktio, jolla tarkistetaan, että sähköposti on oikea sähköposti
def oikeaSPosti(sPosti: str) -> bool:
    if sPosti.find("@") > 0 and sPosti.count("@") == 1 and sPosti.find(".", sPosti.find("@")) != -1 and len(sPosti[sPosti.find("@")+1:]) >= 3:
        return True
    else:
        return False

#Funktio, jolla tarkistetaan, että salasana on kelvollinen
def kelvollinenSalasana(salasana: str) -> bool:
    #Merkkijonot joihin on listattu kaikki sallitut merkit
    sallitutMerkit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:,;-_*?+#!@$<>|/£¤%&{[]}()'"

    #Tarkistetaan että salasana on vähintään kahdeksan merkkiä ja siitä löytyy numero, pieni kirjain ja iso kirjain
    if len(salasana) >= 8 and any(char.isdigit() for char in salasana) == True and any(pikkuKirjain.islower() for pikkuKirjain in salasana) == True and any(isoKirjain.isupper() for isoKirjain in salasana) == True:
        #Tarkistetaan löytyykö jokainen merkki sallituista merkeistä
        for merkki in salasana:
            if merkki in sallitutMerkit:
                return False
    else:
        return False
    
    return True


#Kysytään haluaako käyttäjä kirjautua vai luoda uuden käyttäjän
kirjautuminen = input("Haluatko kirjautua (K) vai luoda uuden käyttäjän (L)? ")

#Käyttäjä haluaa kirjautua
if kirjautuminen == "K" or kirjautuminen == "k":
    sisaankirjautuminen()
#Käyttäjä haluaa luoda uuden käyttäjän
elif kirjautuminen == "L" or kirjautuminen == "l":
    kayttajan_luonti()