import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def carica_corsi(self):
        corsi=self._model.getAllCorsi()
        for corso in corsi:
            self._view.dd_corsi.options.append(ft.dropdown.Option(key=corso.codins,text=corso.__str__()))
            self._view.update_page()

    def handle_cercaIscritti(self,e):
        cod_corso=self._view.dd_corsi.value
        if cod_corso is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare un corso"))
            self._view.update_page()

        iscritti=self._model.getStudentiCorso(cod_corso)
        self._view.txt_result.controls.clear()

        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti",color="blue"))
        for i in iscritti:
            riga_studente=ft.Text(i.__str__())
            self._view.txt_result.controls.append(riga_studente)
        self._view.update_page()

    def handle_cercaStudente(self,e):
        matricola=self._view.txt_matricola.value
        if matricola is None or matricola=="":
            self._view.create_alert("Inserisci una matricola")
            return
        studente=self._model.getStudenteMatricola(matricola)
        self._view.txt_result.controls.clear()
        if studente is None:
            self._view.txt_result.controls.append(ft.Text("Matricola non trovata"))
            self._view.update_page()
            return

        self._view.txt_nome.value=studente._nome
        self._view.txt_cognome.value=studente._cognome
        self._view.txt_result.controls.append(ft.Text(f"Matricola selezionata, {studente}!"))
        self._view.update_page()

    def handle_cercaCorsi(self, e):
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserisci una matricola")
            return
        corsi=self._model.getCorsiMatricola(matricola)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Risultano, {len(corsi)} corsi!"))
        for c in corsi:
            self._view.txt_result.controls.append(ft.Text(c.__str__()))
        self._view.update_page()


    def handle_IscriviStudente(self,e):
        cod_corso = self._view.dd_corsi.value
        if cod_corso is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare un corso"))
            self._view.update_page()
            return
        corso=self._model.getCorso(cod_corso)

        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserisci una matricola")
            return
        studente=self._model.getStudenteMatricola(matricola)
        self._view.txt_result.controls.clear()

        successo = self._model.creaIscrizione( cod_corso,matricola)
        if successo:
            self._view.txt_result.controls.append(ft.Text(f"Studente {studente} iscritto al corso {corso}"))

        else:
            self._view.txt_result.controls.append(ft.Text("Impossibile iscrivere lo studente"))

        self._view.update_page()



