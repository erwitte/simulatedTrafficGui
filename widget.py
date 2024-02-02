import random
from json_parser import JsonParser
from script_caller import ScriptCaller

from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QSpinBox, QComboBox


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.script_caller = ScriptCaller()
        self.json_parser = JsonParser("~/Schreibtisch/alles/PycharmProjects/simulatedTraffic/10.json")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.create_choose_day()
        self.create_choose_speed()
        self.create_choose_display_duration()

        # button leitet einträge weiter und löscht fensterinhalt
        confirm_button = QtWidgets.QPushButton("Bestätigen", self)
        confirm_button.clicked.connect(self.clear_contents)
        self.layout.addWidget(confirm_button)


    def create_choose_day(self):
        number_days = self.json_parser.get_number_of_days()
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

        input_duration = QSpinBox()
        input_duration.setMinimum(0)
        input_duration.setFixedSize(100, 30)
        self.layout.addWidget(input_duration)

        combobox_duration = QComboBox()
        combobox_duration.addItem("Minuten")
        combobox_duration.addItem("Stunden")
        combobox_duration.setFixedSize(100, 30)
        self.layout.addWidget(combobox_duration)

    def clear_contents(self):
        self.script_caller.start_script()
        # Clear all child widgets from the layout
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

