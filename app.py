
from flask import Flask, render_template, request

app = Flask(__name__)

# --- MEMORY (Lesson 3) ---
# A simple list to store words
word_list = ["Python", "Flask", "Code"]

# --- MAPPING (Lesson 4) ---
# A dictionary to store mood responses
mood_responses = {
    "happy": "That is great! Keep smiling!",
    "sad": "I am sorry. I hope your day gets better.",
    "tired": "Rest is important. Maybe take a nap?"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/print')
def print_page():
    # --- PRINT (Lesson 1) ---
    print("LOG: Someone visited the Print page!")
    return render_template('print.html')

@app.route('/if', methods=['GET', 'POST'])
def if_page():
    message = ""
    if request.method == 'POST':
        # --- IF/ELSE (Lesson 2) ---
        age = int(request.form.get('age', 0))
        if age >= 18:
            message = "You are an adult."
        else:
            message = "You are a minor."
    return render_template('if.html', message=message)

@app.route('/list', methods=['GET', 'POST'])
def list_page():
    if request.method == 'POST':
        new_word = request.form.get('word')
        if new_word:
            word_list.append(new_word)
    return render_template('list.html', words=word_list)

@app.route('/dict', methods=['GET', 'POST'])
def dict_page():
    answer = ""
    if request.method == 'POST':
        user_mood = request.form.get('mood', '').lower()
        # Look up the mood in our dictionary
        answer = mood_responses.get(user_mood, "I don't know that mood yet.")
    return render_template('dict.html', answer=answer)

@app.route('/loop', methods=['GET', 'POST'])
def loop_page():
    letters = []
    if request.method == 'POST':
        user_word = request.form.get('word', '')
        # --- FOR LOOP (Lesson 5) ---
        for char in user_word:
            letters.append(char.upper())
    return render_template('loop.html', letters=letters)

if __name__ == '__main__':
    app.run(debug=True)
