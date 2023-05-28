import gradio as gr
import pandas as pd

def display_csv_file(csv_file_name, start_row, end_row, question):
    try:
        df = pd.read_csv(csv_file_name, header=None, delimiter=" ")
        df2 = pd.read_csv(csv_file_name, delimiter=" ")
        start_row = int(start_row)
        end_row = int(end_row)
        print(question)
        if start_row > end_row:
            return "Numer pierwszego wiersza powinien być mniejszy niż numer ostatniego wiersza."
        elif start_row < 1 or end_row > len(df):
            return "Numer wiersza poza zakresem."
        else:

            return df[start_row-1:end_row].to_string(index=False, header=False), end_row-start_row+1, len(df2.columns), ile(df, df2) if question=="Ile jest klas decyzyjnych?" else ile2(df, df2) if question=="Jaka jest wielkość każdej klasy decyzyjnej?" else "nie wybrales dodatowego pytania"
    except FileNotFoundError:
        return "Nie znaleziono pliku o podanej nazwie!"


def ile(df, df2): 
    return df[len(df2.columns)-1].nunique()

def ile2(df, df2):
    return df[len(df2.columns)-1].value_counts()


iface = gr.Interface(
    fn=display_csv_file,
    inputs=[gr.inputs.Textbox("text", label="Nazwa pliku"),
            gr.inputs.Textbox("number", label="Numer rzędu startowegp"),
            gr.inputs.Textbox("number", label="Numer rzędu końcowego"), 
            gr.inputs.Dropdown(("Ile jest klas decyzyjnych?", "Jaka jest wielkość każdej klasy decyzyjnej?"), label="Dodatkowe informacje dotyczace calego pliku")],
    outputs=[gr.outputs.Textbox(label="Wynik"),
              gr.outputs.Textbox(label="Ilosc wyswietlonych obiektow"), 
              gr.outputs.Textbox(label="Ilosc wyswietlonych atrybutow"),
              gr.outputs.Textbox(label="Dodatkowe pytanie")
              ],
    title="Wyświetl plik CSV",
    description="Program umożliwia wyświetlenie wybranych wierszy z pliku CSV.",
    examples=[
        ["australian.txt", "1", "5", "Jaka jest wielkość każdej klasy decyzyjnej?"],
        ["nursery.txt", "5", "20", "Ile jest klas decyzyjnych?"]
    ]
)

iface.launch()