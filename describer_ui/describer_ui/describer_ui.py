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
                          "Photo", on_click=lambda: rx.redirect("/photo"),
                          width="500px", height="400px",
                          font_size="35px", background_color="#b25938", ),
                rx.button(rx.icon(tag="clipboard-pen"),
                          "Text", on_click=lambda: rx.redirect("/text"),
                          width="500px", height="400px",
                          font_size="35px", background_color="#c2b280", ),
                spacing="5",
            ),
            height="70vh",
        ),
    )


def photo_page() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                rx.center(
                    rx.heading("Photo Page", size="8", color="white"),
                    height="10vh"
                ),
                rx.upload(
                    rx.vstack(
                        rx.button(
                            "Select File",
                            size="4",
                            color="white",
                            bg="#111113",
                            width="100%",
                            height="100%",
                            color_scheme='gray'
                        ),
                    ),
                    id="upload1",
                    border=f"1px solid white",
                    border_radius="10px",
                    width="500px",
                    height="190px",
                    align_items="center",
                    justify_content="center",

                ),
                rx.input(
                    placeholder="Write a description here...",
                    width="500px",
                    color_scheme='gray',
                    variant="soft",
                ),
            ),
        ),
    )


def text_page() -> rx.Component:
    return rx.container(
        rx.center(
            rx.heading("Text Page", size="8"),
            height="20vh"
        ),
        height="100%",
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(photo_page, route="/photo")
app.add_page(text_page, route="/text")
