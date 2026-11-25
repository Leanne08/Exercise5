import os
from PySide6.QtWidgets import QWidget, QComboBox, QPushButton, QLabel
from PySide6.QtGui import QPixmap
import matplotlib.pyplot as plt


class MessageWindow(QWidget):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Notice")
        self.setGeometry(400, 320, 320, 140)

        with open("style.qss") as f:
            self.setStyleSheet(f.read())

        self.lbl = QLabel(text, self)
        self.lbl.setGeometry(25, 25, 270, 40)

        self.ok_btn = QPushButton("OK", self)
        self.ok_btn.setGeometry(110, 80, 100, 35)
        self.ok_btn.clicked.connect(self.close)


class GraphWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Graph Window")
        self.setGeometry(250, 200, 660, 430)

        with open("style.qss") as f:
            self.setStyleSheet(f.read())

        self.msg_window = None
        self.fig, self.ax = plt.subplots(figsize=(4.4, 3.9), dpi=100)
        self.setupUI()
        self.clear_graph()

    def setupUI(self):
        self.graph_label = QLabel(self)
        self.graph_label.setGeometry(20, 20, 440, 390)

        self.body_combo = QComboBox(self)
        self.body_combo.setGeometry(480, 30, 150, 40)
        self.body_combo.addItems(["Body 1", "Body 2"])

        self.draw_btn = QPushButton("Draw", self)
        self.draw_btn.setGeometry(480, 90, 150, 45)
        self.draw_btn.clicked.connect(self.draw_graph)

        self.clear_btn = QPushButton("Clear", self)
        self.clear_btn.setGeometry(480, 150, 150, 45)
        self.clear_btn.clicked.connect(self.clear_graph)

        self.export_btn = QPushButton("Export to CSV", self)
        self.export_btn.setGeometry(480, 210, 150, 45)
        self.export_btn.clicked.connect(self.export_to_csv)

    def show_message(self, text):
        self.msg_window = MessageWindow(text)
        self.msg_window.show()

    def update_graph_image(self):
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Temperature (°C)")
        self.fig.savefig("temp_graph.png")
        self.graph_label.setPixmap(QPixmap("temp_graph.png"))

    def draw_graph(self):
        times = self.main_window.time_history
        if len(times) == 0:
            self.show_message("No simulation data available yet.")
            return

        selected = self.body_combo.currentText()
        if selected == "Body 1":
            temps = self.main_window.body1_temp_history
            color = "red"
        else:
            temps = self.main_window.body2_temp_history
            color = "blue"

        self.ax.plot(times, temps, label=selected, color=color, linewidth=2)
        self.ax.legend()
        self.update_graph_image()

    def clear_graph(self):
        self.ax.clear()
        self.update_graph_image()

    def export_to_csv(self):
        times = self.main_window.time_history
        t1_list = self.main_window.body1_temp_history
        t2_list = self.main_window.body2_temp_history

        if len(times) == 0:
            self.show_message("No data to export yet.")
            return

        filename = "heat_transfer_results.csv"
        with open(filename, "w") as file:
            file.write("Time (s),Body 1 Temp (°C),Body 2 Temp (°C)\n")
            for i in range(len(times)):
                line = f"{round(times[i], 3)},{round(t1_list[i], 3)},{round(t2_list[i], 3)}\n"
                file.write(line)

        os.startfile(filename)