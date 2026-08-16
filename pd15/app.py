# Bibliotecas
from shiny import ui, render, App
from bcb import currency
import pandas as pd

# Interface do Usuário
app_ui = ui.page_navbar(
    ui.nav_panel(
        "📊",
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select(
                    id ="moeda",
                    label = "Moeda",
                    choices = currency.get_currency_list().symbol.sort_values().to_list(),
                    selected="AUD"
                ),
                ui.input_date_range(
                    id="periodo",
                    label="Data Inicial e Final:",
                    start= (pd.to_datetime("today")- pd.offsets.MonthBegin(24)).strftime("%Y-%m-%d"),
                    end= pd.to_datetime("today").strftime("%Y-%m-%d"),
                    max = pd.to_datetime("today").strftime("%Y-%m-%d"),
                    language="pt-BR",
                    separator="-"
                ),
                width = 275 

            ),
            ui.card("output")
        )
    ),
    title="Câmbio App"
)


#Servidor
def server(input, output, session):
    ...



#Dashboard Shiny
app = App(app_ui, server)