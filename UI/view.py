import flet as ft
from model import corso

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_corsi = None
        self.corsi=None
        self.btn_matricola = None
        self.txt_nome = None
        self.txt_cognome= None

        self.btn_cercaIscritti=None
        self.btn_cercaStudente=None
        self.btn_cercaCorso=None
        self.btn_iscriviStudente=None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name

        self.dd_corsi=ft.Dropdown(
            label="Corso", hint_text="Selezionare un corso", options=[],width=1000
        )

        self.txt_matricola = ft.TextField(
            label="matricola",
            width=200,
            hint_text="Inserisci una matricola"
        )
        self.txt_nome=ft.TextField(label="Nome", read_only=True)
        self.txt_cognome = ft.TextField(label="Cognome", read_only=True)


        # button
        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_cercaIscritti)

        row1 = ft.Row([self.dd_corsi, self.btn_cercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        row2=ft.Row([self.txt_matricola,self.txt_nome,self.txt_cognome],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btn_cercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_cercaStudente)
        self.btn_cercaCorso = ft.ElevatedButton(text="Cerca corso",
                                                   on_click=self._controller.handle_cercaCorsi)
        self.btn_iscriviStudente = ft.ElevatedButton(text="Iscrivi studente",
                                                   on_click=self._controller.handle_IscriviStudente)
        row3=ft.Row([self.btn_cercaStudente,self.btn_cercaCorso,self.btn_iscriviStudente],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
