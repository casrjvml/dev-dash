# Bibliotecas
from shiny import App, render, ui
import pandas as pd 

# Dados

dados = (
    pd.read_json(
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/01/2017"
    )
    .assign(data=lambda x: pd.to_datetime(x["data"], format="%d/%m/%Y"))
)

print(dados.head())



# Interface do usuário
app_ui = ui.page_navbar(
   ui.nav_panel(
       "Gráficos",
       ui.layout_columns(
           ui.card("Gráfico estático"),
           ui.card("Gráfico interativo")
           )    
       ), 
   title= "Visualização de Dados"
)

# Servidor
def server(input, output, session):
    ...

# Shiny Dashboard
app = App(app_ui, server)
