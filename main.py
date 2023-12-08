import PyPDF2
import tkinter as tk
from tkinter import filedialog, simpledialog

def main():
    root = tk.Tk()
    root.withdraw() # Versteckt das Hauptfenster von Tkinter

    # Öffnen eines Dialogfensters zur Auswahl der Eingabedatei
    input_path = filedialog.askopenfilename(title="Wählen Sie die PDF-Datei aus", filetypes=[("PDF Files", "*.pdf")])
    if not input_path:
        return

    # Abfrage der Anzahl der Duplikate
    number_of_copies = simpledialog.askinteger("Anzahl der Duplikate", "Geben Sie die Anzahl der Duplikate ein:", minvalue=1, maxvalue=1000)
    if not number_of_copies:
        return

    # Öffnen eines Dialogfensters zur Festlegung des Ausgabepfads
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Speichern als", filetypes=[("PDF Files", "*.pdf")])
    if not output_path:
        return

    # Öffnen des PDFs
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Wählen Sie die zu duplizierende Seite (z.B. Seite 1)
        page = reader.pages[0]

        # Duplizieren Sie die Seite entsprechend der Anzahl
        for _ in range(number_of_copies):
            writer.add_page(page)

        # Schreiben Sie das neue PDF
        with open(output_path, 'wb') as output_pdf:
            writer.write(output_pdf)

if __name__ == "__main__":
    main()
