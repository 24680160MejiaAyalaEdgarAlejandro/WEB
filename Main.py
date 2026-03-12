import flet as ft
import random

def main(page: ft.Page):
    # Configuraciones específicas para que se vea bien en el navegador
    page.title = "Juego PPT - Web"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 50

    # Variables de estado
    opciones = ["Piedra", "Papel", "Tijera"]
    puntos_usuario = [0]
    puntos_cpu = [0]
    
    # Elementos de la interfaz
    titulo = ft.Text("¡Piedra, Papel o Tijera!", size=35, weight="bold", color=ft.Colors.BLUE)
    marcador = ft.Text("Tú: 0 | CPU: 0", size=22, weight="w500")
    resultado = ft.Text("Elige una opción para jugar", size=18, italic=True)

    def jugar(e):
        eleccion_usuario = e.control.text
        eleccion_cpu = random.choice(opciones)
        
        if eleccion_usuario == eleccion_cpu:
            mensaje = f"Empate, ambos eligieron {eleccion_usuario}"
        elif (eleccion_usuario == "Piedra" and eleccion_cpu == "Tijera") or \
             (eleccion_usuario == "Papel" and eleccion_cpu == "Piedra") or \
             (eleccion_usuario == "Tijera" and eleccion_cpu == "Papel"):
            mensaje = f"¡Ganaste! {eleccion_usuario} vence a {eleccion_cpu}"
            puntos_usuario[0] += 1
        else:
            mensaje = f"Perdiste... {eleccion_cpu} vence a {eleccion_usuario}"
            puntos_cpu[0] += 1
        
        resultado.value = mensaje
        marcador.value = f"Tú: {puntos_usuario[0]} | CPU: {puntos_cpu[0]}"
        page.update()

    # Botones con iconos para que se vea más moderno en web
    botones = ft.Row(
        [
            ft.Button("Piedra", icon=ft.Icons.BRIGHTNESS_5, on_click=jugar),
            ft.Button("Papel", icon=ft.Icons.DESCRIPTION, on_click=jugar),
            ft.Button("Tijera", icon=ft.Icons.CONTENT_CUT, on_click=jugar),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Agregar todo a la página
    page.add(
        ft.Column(
            [
                titulo,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                marcador,
                resultado,
                ft.Divider(height=20),
                botones,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# ESTO ES LO MÁS IMPORTANTE PARA NETLIFY/WEB:
# Flet necesita saber que se ejecutará en el puerto del navegador
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)