import flet as ft

def main(page : ft.page):
    page.title = "Olá, Flet!"
    page.vertical_aligment = ft.MainAxisAlignment.CENTER

    lbl_ola = ft.Text("Olá, MergeSkills!", size=40, weight="bold", color="blue")

    def on_click(e):
        lbl_ola.value = "Botão Clicado!"
        page.update()

    btn = ft.Button("Clique aqui", on_click=on_click)

    page.add(lbl_ola, btn)


ft.run(main)