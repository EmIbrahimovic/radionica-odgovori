
from flask import Flask, render_template, request

app = Flask(__name__)

# --- MEMORIJA (Lekcija 3) ---
# Jednostavna lista za pohranu riječi
lista_rijeci = ["Python", "Flask", "Kod"]

# --- MAPIRANJE (Lekcija 4) ---
# Rječnik sa proizvoljnim riječima i njihovim značenjima
rjecnik_pojmova = {
    "varijabla": "Kontejner za pohranu podataka.",
    "funkcija": "Blok koda koji se izvršava samo kada se pozove.",
    "petlja": "Način da se dio koda ponovi više puta.",
    "lista": "Kolekcija podataka poredanih u niz.",
    "rjecnik": "Kolekcija ključeva i vrijednosti."
}

@app.route('/')
def pocetna():
    return render_template('index.html')

@app.route('/ispis')
def ispis_stranica():
    # --- PRINT (Lekcija 1) ---
    print("LOG: Neko je posjetio stranicu za ispis!")
    return render_template('print.html')

@app.route('/varijabla')
def varijabla_stranica():
    # --- VARIJABLA (Lekcija 1.2) ---
    # TODO (UČENIK):
    # Promijeni vrijednost ove varijable
    poruka = "Zdravo iz backend-a!"

    return render_template('variable.html', poruka=poruka)

@app.route('/unos', methods=['GET', 'POST'])
def unos_stranica():
    uneseni_tekst = ""

    if request.method == 'POST':
        # --- INPUT IZ FORME (Lekcija 2.2) ---
        # TODO (UČENIK):
        # Dohvati tekst koji je korisnik upisao u input polje
        uneseni_tekst = request.form.get('tekst', '')

    return render_template('input.html', uneseni_tekst=uneseni_tekst)


@app.route('/ako', methods=['GET', 'POST'])
def ako_stranica():
    poruka = ""
    if request.method == 'POST':
        # --- IF/ELSE (Lesson 2) ---
        godine = int(request.form.get('godine', 0))
        if godine >= 18:
            poruka = "Vi ste punoljetni."
        else:
            poruka = "Vi ste maloljetni."
    return render_template('if.html', poruka=poruka)

@app.route('/lista', methods=['GET', 'POST'])
def lista_stranica():
    if request.method == 'POST':
        nova_rijec = request.form.get('rijec')
        if nova_rijec:
            lista_rijeci.append(nova_rijec)
    return render_template('list.html', rijeci=lista_rijeci)

@app.route('/rjecnik', methods=['GET', 'POST'])
def rjecnik_stranica():
    odgovor = ""
    pretraga = ""
    if request.method == 'POST':
        pretraga = request.form.get('pojam', '').lower()
        # Potraži pojam u našem rječniku
        odgovor = rjecnik_pojmova.get(pretraga, "Izvinite, taj pojam nemamo u bazi.")
    return render_template('dict.html', odgovor=odgovor, pretraga=pretraga)

@app.route('/petlja', methods=['GET', 'POST'])
def petlja_stranica():
    slova = []
    if request.method == 'POST':
        korisnikova_rijec = request.form.get('rijec', '')
        # --- FOR PETLJA (Lesson 5) ---
        for znak in korisnikova_rijec:
            slova.append(znak.upper())
    return render_template('loop.html', slova=slova)

if __name__ == '__main__':
    app.run(debug=True)
