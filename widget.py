import webbrowser

from data_parser import DataParser
from script_caller import ScriptCaller

from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QSpinBox, QComboBox, QCheckBox


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.checkbox_layout = None
        self.input_duration = None
        self.script_caller = ScriptCaller()
        self.data_parser = DataParser("~/Schreibtisch/alles/PycharmProjects/simulatedTraffic/10.json")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.populate()

    def populate(self):
        self.create_choose_day()
        self.create_choose_speed()
        self.create_choose_display_duration()
        self.create_open_file_checkbox()

        # button leitet einträge weiter und lädt farbbalken
        confirm_button = QtWidgets.QPushButton("Bestätigen", self)
        confirm_button.clicked.connect(self.clear_contents)
        self.layout.addWidget(confirm_button)

    def populate_after_1st_time(self):
        # deletes back btn
        # index keeps changing so loop necessary
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        self.populate()

    def create_choose_day(self):
        number_days = self.data_parser.get_number_of_days()
        choose_days_label = QLabel("Tag wählen")
        choose_days_label.setFixedSize(200, 30)
        self.layout.addWidget(choose_days_label)
        combobox_choose_days = QComboBox()

        for day_counter in range(number_days):
            combobox_choose_days.addItem(str(day_counter + 1))

        combobox_choose_days.setFixedSize(100, 30)
        self.layout.addWidget(combobox_choose_days)

    def create_choose_speed(self):
        speed_label = QLabel("Fortschrittsgeschwingkeit eingeben")
        speed_label.setFixedSize(200, 30)
        self.layout.addWidget(speed_label)

        input_speed = QSpinBox()
        input_speed.setMinimum(0)
        input_speed.setFixedSize(100, 30)
        self.layout.addWidget(input_speed)

        combobox_speed = QComboBox()
        combobox_speed.addItem("Minuten")
        combobox_speed.addItem("Stunden")
        combobox_speed.setFixedSize(100, 30)
        self.layout.addWidget(combobox_speed)

    def create_choose_display_duration(self):
        duration_label = QLabel("Darstellungsdauer eingeben")
        duration_label.setFixedSize(200, 30)
        self.layout.addWidget(duration_label)

        self.input_duration = QSpinBox()
        self.input_duration.setMinimum(0)
        self.input_duration.setFixedSize(100, 30)
        self.layout.addWidget(self.input_duration)

        combobox_duration = QComboBox()
        combobox_duration.addItem("Minuten")
        combobox_duration.addItem("Stunden")
        combobox_duration.setFixedSize(100, 30)
        self.layout.addWidget(combobox_duration)

    def create_open_file_checkbox(self):
        self.checkbox_layout = QtWidgets.QHBoxLayout(self)

        open_file_label = QLabel("Datei automatisch öffnen")
        open_file_label.setFixedSize(200, 30)
        self.checkbox_layout.addWidget(open_file_label)

        open_file_checkbox = QCheckBox()
        open_file_checkbox.setChecked(False)
        self.checkbox_layout.addWidget(open_file_checkbox)

        self.layout.addLayout(self.checkbox_layout)

    def get_input(self):
        inputted_values = []
        print(self.input_duration.value())

    def clear_contents(self):
        self.get_input()
        self.script_caller.start_script()
        webbrowser.open("marker.html")
        # Clear all child widgets from layout
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        # clears all child widgets fron checkbox_layout
        for i in reversed(range(self.checkbox_layout.count())):
            widget = self.checkbox_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        back_btn = QtWidgets.QPushButton("zurück", self)
        back_btn.clicked.connect(self.populate_after_1st_time)
        self.layout.addWidget(back_btn)

    def call_script(self):
        print("isjg")




