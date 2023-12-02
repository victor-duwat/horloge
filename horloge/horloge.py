import tkinter as tk
from tkinter import simpledialog
import time

class HorlogeDigitaleGUI:
    def __init__(self, root):
        self.root = root
        root.title("Horloge Digitale")

        root.configure(bg='light grey')
        font_heure = ('Helvetica', 48)
        font_boutons = ('Helvetica', 14)

        self.label_heure = tk.Label(root, font=font_heure, fg='navy', bg='white', padx=20, pady=20)
        self.label_heure.pack(pady=10)

        frame_boutons = tk.Frame(root, bg='light grey')
        frame_boutons.pack(pady=10)

        self.bouton_regler_heure = tk.Button(frame_boutons, text="Régler Heure", font=font_boutons, command=self.regler_heure)
        self.bouton_regler_heure.pack(side=tk.LEFT, padx=5)

        self.bouton_regler_alarme = tk.Button(frame_boutons, text="Régler Alarme", font=font_boutons, command=self.regler_alarme)
        self.bouton_regler_alarme.pack(side=tk.LEFT, padx=5)

        self.bouton_pause = tk.Button(frame_boutons, text="Pause", font=font_boutons, command=self.basculer_pause)
        self.bouton_pause.pack(side=tk.LEFT, padx=5)

        self.bouton_changer_format = tk.Button(frame_boutons, text="Changer Format", font=font_boutons, command=self.changer_format)
        self.bouton_changer_format.pack(side=tk.LEFT, padx=5)

        self.format_24h = True
        self.en_pause = False
        self.heure_alarme = None
        self.mise_a_jour()

    def mise_a_jour(self):
        if not self.en_pause:
            self.heure_actuelle = time.localtime()
            self.afficher_heure()
            self.verifier_alarme()
        self.root.after(1000, self.mise_a_jour)

    def afficher_heure(self):
        heure_formattee = time.strftime("%H:%M:%S" if self.format_24h else "%I:%M:%S %p", self.heure_actuelle)
        self.label_heure.config(text=heure_formattee)

    def regler_heure(self):
        heure = simpledialog.askstring("Régler Heure", "Entrer l'heure (hh:mm:ss):")
        if heure:
            h, m, s = map(int, heure.split(':'))
            self.heure_actuelle = time.struct_time((2023, 1, 1, h, m, s, 0, 0, -1))

    def regler_alarme(self):
        heure = simpledialog.askstring("Régler Alarme", "Entrer l'heure de l'alarme (hh:mm:ss):")
        if heure:
            self.heure_alarme = tuple(map(int, heure.split(':')))

    def verifier_alarme(self):
        if self.heure_alarme:
            h, m, s = self.heure_alarme
            if (self.heure_actuelle.tm_hour, self.heure_actuelle.tm_min, self.heure_actuelle.tm_sec) == (h, m, s):
                tk.messagebox.showinfo("Alarme", "L'heure de l'alarme est arrivée !")
                self.heure_alarme = None 

    def basculer_pause(self):
        self.en_pause = not self.en_pause
        self.bouton_pause.config(text="Reprendre" if self.en_pause else "Pause")

    def changer_format(self):
        self.format_24h = not self.format_24h

root = tk.Tk()
app = HorlogeDigitaleGUI(root)
root.mainloop()
