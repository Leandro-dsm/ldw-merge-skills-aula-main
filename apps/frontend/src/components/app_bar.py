import flet as ft  # Importa a biblioteca Flet para criação de interfaces

# Função que constrói uma AppBar (barra superior do app)
def build_app_bar(
    title: str,                  # Título principal da barra
    subtitle: str | None = None, # Subtítulo opcional
    show_back: bool = False,     # Define se o botão de voltar será exibido
    on_back=None,                # Função chamada ao clicar no botão voltar
) -> ft.Control:                # Retorna um componente do Flet

    # Lista que armazenará os elementos do lado esquerdo (botão + textos)
    left_controls: list[ft.Control] = []

    # Se for para mostrar o botão de voltar e existir uma função associada
    if show_back and on_back is not None:
        left_controls.append(
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,  # Ícone de seta para voltar
                icon_color="#111111",      # Cor do ícone
                on_click=on_back,          # Evento de clique
            )
        )

    # Lista que armazena os textos (título e subtítulo)
    text_column = [
        ft.Text(
            title,                      # Texto principal
            size=20,                    # Tamanho maior
            weight=ft.FontWeight.W_700, # Negrito
            color="#111111"             # Cor (corrigido: faltava #)
        ),
    ]

    # Se houver subtítulo, adiciona abaixo do título
    if subtitle:
        text_column.append(
            ft.Text(
                subtitle,               # Texto secundário
                size=12,                # Fonte menor
                color="#71717A"         # Cor cinza
            )
        )

    # Adiciona a coluna de textos ao lado esquerdo
    left_controls.append(
        ft.Column(
            controls=text_column,  # Lista de textos
            spacing=2,             # Espaçamento entre eles
            expand=True            # Ocupa o espaço disponível
        )
    )

    # Retorna o container final da AppBar
    return ft.Container(
        content=ft.Row(
            controls=left_controls,                # Botão + textos
            alignment=ft.MainAxisAlignment.START, # Alinhado à esquerda
            vertical_alignment=ft.CrossAxisAlignment.CENTER, # Centralizado verticalmente
        ),
        padding=ft.Padding.symmetric(
            horizontal=8,  # Espaço nas laterais
            vertical=8     # Espaço em cima/baixo
        ),
    )