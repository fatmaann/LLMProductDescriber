import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""
    ...


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(rx.heading("Welcome to LLM Product Describer!", size="8"), height="20vh"),
        rx.center(
            rx.hstack(
                rx.button(rx.icon(tag="image-up"),
                          "Photo", on_click=lambda: rx.window_alert("Photo"), width="500px", height="400px",
                          font_size="35px", background_color="#c7522a", ),
                rx.button(rx.icon(tag="clipboard-pen"),
                          "Text", on_click=lambda: rx.window_alert("Text"), width="500px", height="400px",
                          font_size="35px", background_color="#e5c185", ),
                spacing="5",
            ),
            height="70vh",
        ),
    )


app = rx.App()
app.add_page(index)
