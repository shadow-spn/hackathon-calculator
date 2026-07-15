import tkinter as tk
import re

def calculer(event=None):
    expression = entry.get().strip()

    if not expression:
        resultat_label.config(text="Erreur : veuillez entrer une expression.", fg="#ef4444")
        return

    expression = expression.replace("x", "*").replace("X", "*")

    if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
        resultat_label.config(
            text="Erreur : caractères non autorisés.",
            fg="#ef4444"
        )
        return

    expression = re.sub(r'\b0+(?=\d)', '', expression)

    try:
        resultat = eval(expression)
        
        if isinstance(resultat, float) and resultat.is_integer():
            resultat = int(resultat)

        resultat_label.config(
            text=f"= {resultat}",
            fg="#10b981"
        )

    except ZeroDivisionError:
        resultat_label.config(
            text="Erreur : division par zéro.",
            fg="#ef4444"
        )

    except SyntaxError:
        resultat_label.config(
            text="Erreur : expression invalide.",
            fg="#ef4444"
        )

    except Exception:
        resultat_label.config(
            text="Erreur lors du calcul.",
            fg="#ef4444"
        )

fenetre = tk.Tk()
fenetre.title("Calculatrice Intelligente")
fenetre.geometry("450x260")
fenetre.resizable(False, False)
fenetre.configure(bg="#0a0b10")

cadre = tk.Frame(fenetre, bg="#1e2235", padx=30, pady=30)
cadre.place(relx=0.5, rely=0.5, anchor="center", width=400, height=250)

titre = tk.Label(
    cadre,
    text="Calculatrice",
    font=("Segoe UI", 16, "bold"),
    bg="#1e2235",
    fg="#cbd5e1"
)
titre.pack(pady=(0, 15))

entry = tk.Entry(
    cadre,
    font=("Segoe UI", 14),
    bg="#0f111a",
    fg="#ffffff",
    insertbackground="white",
    relief="flat",
    justify="center"
)
entry.pack(fill="x", ipady=8, pady=(0, 15))
entry.bind('<Return>', calculer)

bouton = tk.Button(
    cadre,
    text="Calculer",
    command=calculer,
    font=("Segoe UI", 12, "bold"),
    bg="#3b82f6",
    fg="white",
    activebackground="#2563eb",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
bouton.pack(fill="x", ipady=5)

resultat_label = tk.Label(
    cadre,
    text="Entrez une expression",
    font=("Segoe UI", 12, "bold"),
    bg="#1e2235",
    fg="#94a3b8"
)
resultat_label.pack(pady=(15, 0))

entry.focus()

fenetre.mainloop()