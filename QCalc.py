from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout, QWidget
from QIconCheckbox import QIconCheckbox
from QElementRow import QElementRow
from QDescriptionRow import QDescriptionRow

app = QApplication([])
window = QWidget()

layout = QHBoxLayout()

layout.addWidget(QDescriptionRow())
layout.addWidget(QElementRow())

window.setLayout(layout)

#window.setFixedSize(window.size())

window.show()
app.exec_()