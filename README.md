# Radionica: Flask vježbe za učenike

Ovaj projekt je jednostavna web-aplikacija napravljena u Flasku, namijenjena učenicima za učenje osnovnih koncepata programiranja: ispis, uvjetne naredbe, rad s listama i rječnicima, te petljama.

**Ciljevi**:
- Razumjeti kako Flask prikazuje HTML predloške.
- Vježbati `print`, `if/else`, liste, rječnike i `for` petlje u praktičnom kontekstu.

**Što je u projektu**:
- `app.py`: glavni Flask program koji pokreće aplikaciju i rute za svaku lekciju.
- `requirements.txt`: potrebne Python biblioteke (samo Flask).
- `templates/`: HTML predlošci za svaku lekciju:
	- `index.html` — početna stranica
	- `print.html` — primjer ispisa i logiranja
	- `if.html` — primjer `if/else` na obrascu
	- `list.html` — rad s listom riječi (dodavanje)
	- `dict.html` — primjer rječnika (mapiranje odgovora)
	- `loop.html` — primjer `for` petlje (razdvajanje slova)
- `static/style.css`: osnovni stilovi.

Kako pokrenuti (Windows PowerShell):

```powershell
python -m venv venv
.
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Otvorite preglednik na: `http://127.0.0.1:5000/`

Ako koristite cmd (Windows):

```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python app.py
```

Kratki pregled lekcija i zadaci za vježbu:
- Lekcija 1 — `print`: posjetite stranicu `Print` i promatrajte ispis u terminalu; dodajte vlastiti `print` u `app.py`.
- Lekcija 2 — `if/else`: pokušajte promijeniti prag (npr. 21) i testirajte različite ulaze.
- Lekcija 3 — `list`
- Lekcija 4 — `dict`: dodajte nove raspoloženja i odgovore u `mood_responses`.
- Lekcija 5 — `loop`: promijenite obradu - npr. prikaži indekse znakova ili obrnut redoslijed.

Zadaci za učenike:
1. Dodajte polje za uklanjanje riječi iz liste i implementirajte rutu.
2. Proširite `mood_responses` tako da pamti nove raspoloženja koja korisnik unese.
3. Na stranici `loop` prikažite broj ponavljanja svakog znaka u riječi.

Kako dalje:
- Igrajte se s HTML-om u `templates/` da promijenite izgled i polja.
- Pokušajte spremiti podatke u datoteku umjesto memorijske liste (napredniji zadatak).
