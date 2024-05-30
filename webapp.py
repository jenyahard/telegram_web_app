import flet as ft


def main(page: ft.Page):
    page.title = "WebApp Page"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Text("Welcome to the WebApp Page!", size=40, weight=ft.FontWeight.BOLD),
        ft.Text("This is a simple web page served by Flet.", size=20),
    )

ft.app(target=main, view=ft.WEB_BROWSER)
