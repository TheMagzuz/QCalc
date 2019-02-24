from PyQt5.QtWidgets import QApplication, QLabel
from QIconCheckbox import QIconCheckbox

app = QApplication([])
button = QIconCheckbox(False)

button.show()
app.exec_()