from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QDoubleSpinBox, QPushButton
from PySide6.QtCore import Qt, QTimer
from Body import Body
from AboutWindow import AboutWindow


class HeatTransfer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Heat Transfer")
        self.setGeometry(200, 150, 740, 430)

        with open("style.qss") as f:
            self.setStyleSheet(f.read())

        self.about_window = AboutWindow()

        self.body1 = None
        self.body2 = None
        self.dt_ms = 50
        self.dt = self.dt_ms / 1000.0
        self.elapsed_time = 0.0
        self.updating_from_timer = False

        self.time_history = []
        self.body1_temp_history = []
        self.body2_temp_history = []

        self.timer = QTimer(self)

        self.setupUI()


    def setupUI(self):
        self.left_slider = QSlider(Qt.Orientation.Vertical, self)
        self.left_slider.setGeometry(45, 40, 25, 170)
        self.left_slider.setRange(0, 200)
        self.left_slider.setValue(200)

        self.left_body_box = QLabel(self)
        self.left_body_box.setGeometry(85, 40, 125, 170)

        self.left_temp_lbl = QLabel("Temp.", self)
        self.left_temp_lbl.setGeometry(35, 235, 55, 30)
        self.left_temp_spin = QDoubleSpinBox(self)
        self.left_temp_spin.setGeometry(95, 235, 115, 30)
        self.left_temp_spin.setRange(0.0, 200.0)
        self.left_temp_spin.setValue(200.0)
        self.left_temp_spin.setSuffix(" °C")
        self.left_temp_spin.setReadOnly(True)

        self.left_mass_lbl = QLabel("Mass", self)
        self.left_mass_lbl.setGeometry(35, 280, 55, 30)
        self.left_mass_spin = QDoubleSpinBox(self)
        self.left_mass_spin.setGeometry(95, 280, 115, 30)
        self.left_mass_spin.setRange(0.01, 10000.0)
        self.left_mass_spin.setValue(10.00)
        self.left_mass_spin.setSuffix(" kg")

        self.left_hcap_lbl = QLabel("H. Cap.", self)
        self.left_hcap_lbl.setGeometry(35, 325, 55, 30)
        self.left_hcap_spin = QDoubleSpinBox(self)
        self.left_hcap_spin.setGeometry(95, 325, 115, 30)
        self.left_hcap_spin.setRange(0.01, 10000.0)
        self.left_hcap_spin.setValue(0.40)
        self.left_hcap_spin.setSuffix(" J/kg°C")

        self.cond_lbl = QLabel("Conductivity", self)
        self.cond_lbl.setGeometry(325, 40, 100, 25)

        self.conductivity_spin = QDoubleSpinBox(self)
        self.conductivity_spin.setGeometry(310, 70, 120, 32)
        self.conductivity_spin.setRange(0.01, 1000.0)
        self.conductivity_spin.setValue(1.00)
        self.conductivity_spin.setSuffix(" J/s°C")

        self.bridge = QLabel("", self)
        self.bridge.setGeometry(210, 120, 320, 28)

        self.start_btn = QPushButton("Start", self)
        self.start_btn.setCheckable(True)
        self.start_btn.setGeometry(305, 230, 130, 42)

        self.graphs_btn = QPushButton("Graphs", self)
        self.graphs_btn.setGeometry(305, 285, 130, 42)
        self.graphs_btn.clicked.connect(self.open_graph_window)

        self.about_btn = QPushButton("About", self)
        self.about_btn.setGeometry(305, 340, 130, 38)
        self.about_btn.clicked.connect(self.open_about_window)

        self.right_body_box = QLabel(self)
        self.right_body_box.setGeometry(530, 40, 125, 170)

        self.right_slider = QSlider(Qt.Orientation.Vertical, self)
        self.right_slider.setGeometry(670, 40, 25, 170)
        self.right_slider.setRange(0, 200)
        self.right_slider.setValue(0)

        self.right_temp_spin = QDoubleSpinBox(self)
        self.right_temp_spin.setGeometry(530, 235, 115, 30)
        self.right_temp_spin.setRange(0.0, 200.0)
        self.right_temp_spin.setValue(0.0)
        self.right_temp_spin.setSuffix(" °C")
        self.right_temp_spin.setReadOnly(True)
        self.right_temp_lbl = QLabel("Temp.", self)
        self.right_temp_lbl.setGeometry(655, 235, 55, 30)

        self.right_mass_spin = QDoubleSpinBox(self)
        self.right_mass_spin.setGeometry(530, 280, 115, 30)
        self.right_mass_spin.setRange(0.01, 10000.0)
        self.right_mass_spin.setValue(10.00)
        self.right_mass_spin.setSuffix(" kg")
        self.right_mass_lbl = QLabel("Mass", self)
        self.right_mass_lbl.setGeometry(655, 280, 55, 30)

        self.right_hcap_spin = QDoubleSpinBox(self)
        self.right_hcap_spin.setGeometry(530, 325, 115, 30)
        self.right_hcap_spin.setRange(0.01, 10000.0)
        self.right_hcap_spin.setValue(0.40)
        self.right_hcap_spin.setSuffix(" J/kg°C")
        self.right_hcap_lbl = QLabel("H. Cap.", self)
        self.right_hcap_lbl.setGeometry(655, 325, 55, 30)


    def open_graph_window(self):
        self.graph_window.show()

    def open_about_window(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication()
    window = HeatTransfer()
    window.show()
    app.exec()