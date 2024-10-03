import base64
import reflex as rx


class State(rx.State):
    img: list[str] = []

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            base64_str = base64.b64encode(upload_data).decode('utf-8')
            self.img.append(base64_str)

    async def get_description(self):
        if len(self.img) == 0:
            print('get_description empty')
        else:
            for file in self.img:
                print('get_description', len(file))


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(rx.heading("Welcome to LLM Product Describer!", size="8"), height="20vh"),
        rx.center(
            rx.hstack(
                rx.button(rx.icon(tag="image-up"), "Photo", on_click=lambda: rx.redirect("/photo"),
                          width="500px", height="400px", font_size="35px", background_color="#b25938"),
                rx.button(rx.icon(tag="clipboard-pen"), "Text", on_click=lambda: rx.redirect("/text"),
                          width="500px", height="400px", font_size="35px", background_color="#c2b280", ),
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
                    rx.heading("Photo Page", size="9", color="white"),
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
                    max_files=1,
                    border=f"1px solid white",
                    border_radius="10px",
                    width="500px",
                    height="190px",
                    align_items="center",
                    justify_content="center",
                    on_drop=State.handle_upload(rx.upload_files(upload_id="upload1")),
                ),
                rx.input(
                    placeholder="Write a description here...",
                    width="500px",
                    height="40px",
                    color_scheme='gray',
                    variant="soft",
                    font_size='12pt'
                ),
                rx.button("Generate", width="200px", height="40px", color_scheme='gray', font_size='12pt',
                          on_click=State.get_description),
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
