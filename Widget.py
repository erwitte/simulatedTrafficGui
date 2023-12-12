import random

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QLabel, QSpinBox, QComboBox


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        speed_label = QLabel("Fortschrittgeschwingkeit eingeben")
        self.layout.addWidget(speed_label)

        input_speed = QSpinBox()
        input_speed.setMinimum(0)
        self.layout.addWidget(input_speed)

        combobox_speed = QComboBox()
        combobox_speed.addItem("Minuten")
        combobox_speed.addItem("Stunden")
        self.layout.addWidget(combobox_speed)

        duration_label = QLabel("Darstellungsdauer eingeben")
        self.layout.addWidget(duration_label)

        input_duration = QSpinBox()
        input_duration.setMinimum(0)
        self.layout.addWidget(input_duration)

        combobox_duration = QComboBox()
        combobox_duration.addItem("Minuten")
        combobox_duration.addItem("Stunden")
        self.layout.addWidget(combobox_duration)
