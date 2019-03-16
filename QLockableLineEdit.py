from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget, QHBoxLayout
from QIconCheckbox import QIconCheckbox
from PyQt5.QtGui import QDoubleValidator

class QLockableLineEdit(QWidget):
  
  def __init__(self, parent=None, flags=Qt.WindowFlags()):
    super(QLockableLineEdit, self).__init__(parent=parent, flags=flags)
    self.layout = QHBoxLayout(self)

    self.value = 0

    self.lineEdit = QLineEdit()
    self.lineEdit.setValidator(QDoubleValidator(0, 9999, 4, self.lineEdit))
    self.lineEdit.setText("0")
    self.lineEdit.textEdited.connect(self.textEdited)

    self.lockButton = QIconCheckbox(False)

    self.layout.setSpacing(0)
    self.layout.addWidget(self.lineEdit)
    self.layout.addWidget(self.lockButton)

  def textEdited(self, text):
    if not text:
      self.value = 0
      return
    if text[0] == ".":
      text = "0" + text
    self.value = float(text)
    print(self.value)