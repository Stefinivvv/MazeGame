from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt6.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(500, 300)
window.setWindowTitle('Соц опитування')

text = QLabel('Граеш в дота2?')
font = QFont('Arial', 36)
text.setFont(font)

def click_btn_ok():
    text.setText('Класно, я теж граю!')

def click_btn_no():
    text.setText('мені прикро!')

h_line = QHBoxLayout()
btn_ok = QPushButton('так')
btn_no = QPushButton('ні')
h_line.addWidget(btn_ok)
h_line.addWidget(btn_no)

btn_ok.clicked.connect(click_btn_ok)
btn_no.clicked.connect(click_btn_no)

v_line = QVBoxLayout()
v_line.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)
v_line.addLayout(h_line)

window.setLayout(v_line)

window.show()
app.exec()

#зробити додаток||||         pyinstaller --onefile 12345.py

