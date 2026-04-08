import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cercaCorso(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        corso = self._view.txt_name.value
        if corso is None or corso == "":
            self._view.create_alert("Seleziona un corso")
            return
        self._view.txt_result.controls.append(ft.Text(f"Corso selezionato, {corso}!"))
        self._view.update_page()

    def handle_cercaStudente(self,e):
        studente=self._view.txt_matricola.value
        if studente is None or studente=="":
            self._view.create_alert("Inserisci una matricola")
            return

        self._view.txt_result.controls.append(ft.Text(f"Matricola selezionata, {studente}!"))
        self._view.update_page()

    def handle_cercaCorso(self,e):
        pass

    def handle_IscriviStudente(self,e):
        pass


