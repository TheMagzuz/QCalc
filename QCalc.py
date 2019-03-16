from PyQt5.QtWidgets import QApplication, QLabel
from QIconCheckbox import QIconCheckbox
from QLockableLineEdit import QLockableLineEdit

app = QApplication([])
button = QLockableLineEdit()

button.show()
app.exec_()