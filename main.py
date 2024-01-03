import PyPDF2
import tkinter as tk
from tkinter import filedialog, simpledialog

def main():
    root = tk.Tk()
    root.withdraw()

    input_path = filedialog.askopenfilename(title="Wählen Sie die PDF-Datei aus", filetypes=[("PDF Files", "*.pdf")])
    if not input_path:
        return

    number_of_duplicates = simpledialog.askinteger("Anzahl der Duplikate", "Geben Sie die Anzahl der Duplikate ein:", minvalue=1, maxvalue=400)
    if not number_of_duplicates:
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", title="Speichern als", filetypes=[("PDF Files", "*.pdf")])
    if not output_path:
        return

    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Duplizieren der ersten beiden Seiten
        for _ in range(number_of_duplicates):
            for page_number in range(2):
                page = reader.pages[page_number]
                writer.add_page(page)

        with open(output_path, 'wb') as output_pdf:
            writer.write(output_pdf)

if __name__ == "__main__":
    main()
