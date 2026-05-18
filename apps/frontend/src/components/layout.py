# Importa a biblioteca Flet para criação de interfaces gráficas
import flet as ft

# Define uma largura máxima padrão para o conteúdo da página
MAX_WIDTH = 1040

# Função que recebe um conteúdo (componente Flet) e o organiza dentro de um layout padrão
def wrap_page(content: ft.Control) -> ft.Control:
    
    # Retorna um Container (caixa principal da página)
    return ft.Container(
        
        # Dentro do container, usamos uma Row (linha) para centralizar o conteúdo
        content=ft.Row(
            controls=[
                # Container interno que limita a largura do conteúdo
                ft.Container(
                    content=content,      # Conteúdo passado para a função
                    width=MAX_WIDTH,      # Define largura máxima
                    expand=False          # Não expande além da largura definida
                ),
            ],
            
            # Centraliza horizontalmente o conteúdo na tela
            alignment=ft.MainAxisAlignment.CENTER,
            
            # Alinha o conteúdo no topo verticalmente
            vertical_alignment=ft.CrossAxisAlignment.START,
            
            # Faz a Row ocupar todo o espaço disponível
            expand=True,
        ),
        
        # Define a cor de fundo da página (branco)
        bgcolor="#FFFFFF",
        
        # Adiciona espaçamento interno (padding) nas bordas
        padding=ft.Padding.only(
            top=20, 
            right=16, 
            bottom=20, 
            left=16
        ),
        
        # Faz o container ocupar todo o espaço disponível
        expand=True,
    )