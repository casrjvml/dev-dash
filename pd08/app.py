#Bibliotecas
from shiny import App, ui

#Interface do Usuário
app_ui = ui.page_navbar(
    ui.nav_panel("Página 1", "Conteúdo da Página 1"),
    ui.nav_panel("Página 2", "Conteúdo da Página 2"),
    ui.nav_panel("Página 3", "Conteúdo da Página 3"),
    ui.nav_control(ui.a("Análise Macro",href="http://analisemacro.com.br/")),
    ui.nav_menu(
        ui.a(Saiba mais" ,
        ui.nav_control(ui.a("Site",href="http://analisemacro.com.br/")),
        ui.nav_control(ui.a("Blog",href="http://analisemacro.com.br/")),
        ui.nav_control(ui.a("Outros Sites",href="http://analisemacro.com.br/")),
    )
    title= ui.row(
        ui.column(6, ui.img(src="https://aluno.analisemacro.com.br/wp-content/uploads/2025/03/logo-azul-escuro-transparente.png")),
        ui.column(6, "Análise Macro")
    ),
    bg="green",
    inverse= True,
    window_title= "Carlos Castro"
)


# Servidor
def server(input, output, session):
    ...


#Dashboard Shiny
app = App(app_ui, server)
