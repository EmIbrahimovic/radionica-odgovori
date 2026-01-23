
from flask import Flask, render_template, request

# --------------------------------------------------
# INICIJALIZACIJA APLIKACIJE
# --------------------------------------------------
# Ovdje kreiramo Flask aplikaciju.
app = Flask(__name__)

# --------------------------------------------------
# LEKCIJA 3: MEMORIJA (LISTE)
# --------------------------------------------------
# Ova lista "živi" na serveru i pamti riječi
# TODO (UČENIK):
# 1) Promijeni ove rijeci
lista_rijeci = ["Python", "Flask", "Kod"]

# --------------------------------------------------
# LEKCIJA 4: MAPIRANJE (RJEČNICI)
# --------------------------------------------------
# Rječnik povezuje pojam (ključ) sa značenjem (vrijednost)
rjecnik_pojmova = {
    "varijabla": "Kontejner za pohranu podataka.",
    "funkcija": "Blok koda koji se izvršava samo kada se pozove.",
    "petlja": "Način da se dio koda ponovi više puta.",
    "lista": "Kolekcija podataka poredanih u niz.",
    "rjecnik": "Kolekcija ključeva i vrijednosti."
}

# --------------------------------------------------
# POČETNA STRANICA
# --------------------------------------------------
@app.route('/')
def pocetna():
    return render_template('index.html')

# --------------------------------------------------
# LEKCIJA 1.1: PRINT
# --------------------------------------------------
@app.route('/ispis')
def ispis_stranica():
    # TODO (UČENIK):
    # 1) Ispiši poruku u terminal koristeći print()
    # 2) Poruka treba da kaže da je korisnik otvorio ovu stranicu

    print("LOG: Neko je posjetio stranicu za ispis!")
    return render_template('print-1.html')


# --------------------------------------------------
# LEKCIJA 1.2: VARIJABLE
# --------------------------------------------------
@app.route('/varijabla')
def varijabla_stranica():
    # TODO (UČENIK):
    # 1) Promijeni tekst poruke
    # 2) Dodaj print() koji ispisuje poruku u terminal

    poruka = "Zdravo iz backend-a!"

    return render_template('print-2.html', poruka=poruka)

# --------------------------------------------------
# LEKCIJA 1.3: INPUT IZ FORME
# --------------------------------------------------
@app.route('/unos', methods=['GET', 'POST'])
def unos_stranica():
    uneseni_tekst = ""

    if request.method == 'POST':
        # 1) Preuzmi tekst koji je korisnik upisao u input polje
        uneseni_tekst = request.form.get('tekst', '')

        # TODO (UČENIK):
        # 2) Ispiši uneseni tekst u terminal pomoću print()
        print(uneseni_tekst)

    return render_template('print-3.html', uneseni_tekst=uneseni_tekst)


# --------------------------------------------------
# LEKCIJA 2: IF / ELSE
# --------------------------------------------------
@app.route('/ako', methods=['GET', 'POST'])
def ako_stranica():
    poruka = ""
    if request.method == 'POST':
        godine = int(request.form.get('godine', 0))
        if godine >= 18:
            poruka = "Vi ste punoljetni."
        else:
            poruka = "Vi ste maloljetni."
    return render_template('if.html', poruka=poruka)


# --------------------------------------------------
# LEKCIJA 3: LISTE (DODAVANJE I BRISANJE)
# --------------------------------------------------
@app.route('/lista', methods=['GET', 'POST'])
def lista_stranica():
    poruka = ""
    if request.method == 'POST':
        akcija = request.form.get('akcija')

        if akcija == 'dodaj':
            # TODO (UČENIK):
            # 1) Ako nova_rijec postoji:
            #    - dodaj je u lista_rijeci
            #    - postavi poruka na tekst o uspjehu

            nova_rijec = request.form.get('rijec')
            if nova_rijec:
                lista_rijeci.append(nova_rijec)
                poruka = "Riječ dodana u listu."

        elif akcija == 'izbrisi':
            # TODO (UČENIK):
            # 1) Ako je lista prazna:
            #    - postavi poruka da nema šta za brisanje
            # 2) Inače:
            #    - izbriši zadnju riječ iz liste
            #    - postavi poruka o brisanju

            if len(lista_rijeci) == 0:
                poruka="Lista je prazna"
            else:
                lista_rijeci.pop()
                poruka = "Zadnja riječ je izbrisana."

    return render_template('list.html', rijeci=lista_rijeci, poruka=poruka)


# --------------------------------------------------
# LEKCIJA 4: RJEČNICI (PRETRAGA)
# --------------------------------------------------
@app.route('/rjecnik', methods=['GET', 'POST'])
def rjecnik_stranica():
    poruka = ""
    pretraga = ""
    if request.method == 'POST':
        pretraga = request.form.get('pojam', '').lower()
        # TODO (UČENIK):
        # 1) Pronađi pojam u rjecnik_pojmova
        # 2) Ako ne postoji, vrati poruku da pojam nije pronađen

        poruka = rjecnik_pojmova.get(pretraga, "Izvinite, taj pojam nemamo u bazi.")
    
    return render_template('dict.html', odgovor=poruka, pretraga=pretraga)

# --------------------------------------------------
# LEKCIJA 5.1: FOR PETLJA
# --------------------------------------------------
@app.route('/petlja', methods=['GET', 'POST'])
def petlja_stranica():
    slova = []
    if request.method == 'POST':
        korisnikova_rijec = request.form.get('rijec', '')

        # Vježba 1: TODO (UČENIK):
        # 1) Prođi kroz svako slovo u riječi
        # 2) Dodaj slovo u listu slova

        for znak in korisnikova_rijec:
            slova.append(znak)
        
        # Vježba 2: TODO (UČENIK):
        # 1) Prođi kroz svako slovo u riječi u obrnutom redoslijedu
        # 2) Dodaj slovo u listu slova
        
        # for znak in reversed(korisnikova_rijec):
        #     slova.append(znak)
        
    return render_template('petlja-1.html', slova=slova)

# --------------------------------------------------
# LEKCIJA 5.2: PETLJA + IF
# --------------------------------------------------
@app.route('/petlja_samoglasnici', methods=['GET', 'POST'])
def petlja_samoglasnici():
    broj = 0
    if request.method == 'POST':
        rijec = request.form.get('rijec', '')
        # TODO (UČENIK):
        # 1) Prođi kroz svako slovo u riječi
        # 2) Ako je slovo samoglasnik (A, E, I, O, U):
        #    - povećaj brojač
        
        for slovo in rijec:
            if slovo in 'aeiou':
                broj = broj + 1

    return render_template('petlja-2.html', broj=broj)

# --------------------------------------------------
# POKRETANJE SERVERA
# --------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
