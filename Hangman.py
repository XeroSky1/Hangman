import tkinter as tk
from tkinter import messagebox
import random

# Predefinēts vārdu saraksts minēšanai. Datu glabasanas tips
word_list = [
    'dators',
    'monitors',    
    'tastatūra',   
    'pelīte',  
    'skeneris',
    'printeris',
    'modēms',
    'maršrutētājs',
    'operētājsistēma',
    'programmatūra',
    'procesors',
    'serveris',
    'ekrāns',
    'akumulators',
    'antivīruss',
    'internets',
    'datorspēle',
    'datorgrafika',
    'algoritms',
    'programma',
    'telefons',
    'planšete',
    'kods',
    'robots',
    'kamera'
]

secret_word = ''  # Mainīgais glabās minamo vārdu
guessed_letters = ''  # Mainīgais glabās minētos burtus
wrong_guesses = 0  # Mainīgais skaitīs nepareizos minējumus
max_wrong_guesses = 10  # Maksimālais nepareizo minējumu skaits

# Funkcija, kas reseto vai sāk spēli
def reset_game():
    global secret_word, guessed_letters, wrong_guesses # Apzimejam, ka mainisim mainigos ari arpus sis funkcijas.
    secret_word = random.choice(word_list).upper()  # Izvēlas nejaušu vārdu no saraksta un pārvērš to lielajos burtos
    guessed_letters = ''  # Reseto minētos burtus
    for i in range( len(secret_word) ):  # Aizpilda minēto burtu vietu ar svītrām
        guessed_letters = guessed_letters + "_"
    wrong_guesses = 0  # Reseto nepareizo minējumu skaitu
    update_display()  # Atjaunina displeju

# Funkcija, kas atjaunina displeju un pārbauda spēles stāvokli
def update_display():
    display_text = '' # Izveido tuksu mainigo, kur pec tam glabasim izvadamo tekstu
    for letter in guessed_letters:
        if display_text != 0:
            display_text += ' '
        display_text += letter

    status_label.config(text='Miniet burtu! ' + display_text)  # Atjaunina statusa tekstu
    entry.delete(0, tk.END)  # Notīra ievades lauku
    draw_hangman()  # Zīmē karātavas
    check_game_state()  # Pārbauda spēles stāvokli

# Funkcija, kas apstrādā minējumu un atjaunina spēles stāvokli
def guess():
    global wrong_guesses
    letter = entry.get().upper()  # Iegūst ievadīto burtu un pārvērš to lielajos burtos
    if len(letter) != 1 or not letter.isalpha():  # Pārbauda, vai ievadīts tieši viens burts
        messagebox.showerror("Kļūda", "Lūdzu, ievadiet tieši vienu burtu.")
        return
    if letter in secret_word:  # Ja burts ir vārdā, atjaunina minētos burtus
        update_guessed_letters(letter)
    else:
        wrong_guesses += 1  # Ja burts nav vārdā, palielina nepareizo minējumu skaitu
    update_display()  # Atjaunina displeju

def update_guessed_letters(letter):
    global guessed_letters
    updated_letters = ''  # Izveido jaunu stringu minētajiem burtiem
    for i in range(len(secret_word)):  # Aizstāj svītras ar pareizi minētajiem burtiem
        if secret_word[i] == letter:
            updated_letters += letter
        else:
            updated_letters += guessed_letters[i]
    guessed_letters = updated_letters  # Atjaunina minēto burtu mainīgo


def draw_hangman():
    canvas.delete("all")  # Notīra zīmējuma audeklu
    # Zemāk ir nosacījumi, kas zīmē dažādas karātavu daļas atkarībā no nepareizo minējumu skaita
    if wrong_guesses >= 1:
        canvas.create_oval(10, 10, 190, 190, fill="yellow", outline="black", width=2)
    if wrong_guesses >= 2:
        canvas.create_oval(50, 50, 90, 90, fill="white", outline="black", width=2)
    if wrong_guesses >= 3:
        canvas.create_oval(110, 50, 150, 90, fill="white", outline="black", width=2)
    if wrong_guesses >= 4:
        canvas.create_oval(65, 65, 75, 75, fill="black")
    if wrong_guesses >= 5:    
        canvas.create_oval(125, 65, 135, 75, fill="black")
    if wrong_guesses >= 6:
        canvas.create_arc(50, 50, 150, 150, start=230, extent=80, style=tk.ARC, outline="black", width=2)
    if wrong_guesses >= 7:
        canvas.create_oval(60, 80, 70, 120, fill="light blue", outline="light blue")
    if wrong_guesses >= 8:
        canvas.create_oval(130, 80, 140, 120, fill="light blue", outline="light blue")
    if wrong_guesses >= 9:
        canvas.create_oval(130, 120, 140, 190, fill="light blue", outline="light blue")
    if wrong_guesses >= 10:
        canvas.create_oval(60, 120, 70, 190, fill="light blue", outline="light blue")        


# Funkcija, kas pārbauda, vai spēle ir uzvarēta vai zaudēta
def check_game_state():
    win = True  # Pieņem, ka spēlētājs ir uzvarējis
    for letter in guessed_letters:
        if letter == '_':  # Ja ir vismaz viena svītra, spēle vēl nav uzvarēta
            win = False
            break
    
    if win:  # Ja spēlētājs ir uzvarējis, parāda uzvaras ziņojumu un sāk jaunu spēli
        messagebox.showinfo("Uzvara", "Jūs uzminējāt vārdu!")
        reset_game()
    elif wrong_guesses >= max_wrong_guesses:  # Ja spēlētājs ir zaudējis, parāda zaudējuma ziņojumu un sāk jaunu spēli
        messagebox.showinfo("Zaudējāt", "Vārds bija: " + secret_word)
        reset_game()

window = tk.Tk()  # Izveido Tkinter logu
window.title('Karātavas')  # Uzstāda loga virsrakstu

status_label = tk.Label(window, text='Miniet burtu!')  # Izveido statusa etiķeti
status_label.pack()  # Pievieno etiķeti logam

canvas = tk.Canvas(window, width=240, height=240)  # Izveido zīmējuma audeklu
canvas.pack()  # Pievieno audeklu logam

entry = tk.Entry(window)  # Izveido ievades lauku
entry.pack()  # Pievieno ievades lauku logam

guess_button = tk.Button(window, text="Minēt", command=guess)  # Izveido pogu minējumam
guess_button.pack()  # Pievieno pogu logam

reset_game_button = tk.Button(window, text="Sākt jaunu spēli", command=reset_game)  # Izveido pogu spēles restartēšanai
reset_game_button.pack()  # Pievieno restartēšanas pogu logam

reset_game()

window.mainloop()
