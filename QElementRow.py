from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from QLockableLineEdit import QLockableLineEdit

class QElementRow(QWidget):
  def __init__(self, parent=None, flags=Qt.WindowFlags()):
    super().__init__(parent=parent, flags=flags)

    layout = QVBoxLayout()

    self.elementName = QLineEdit("")

    self.elementRatio = QLockableLineEdit()

    self.amount = QLockableLineEdit()

    self.mass = QLockableLineEdit()

    self.molarWeight = QLockableLineEdit()

    self.concentration = QLockableLineEdit()

    self.volume = QLockableLineEdit()


    layout.addWidget(self.elementName)
    layout.addWidget(self.elementRatio)
    layout.addWidget(self.amount)
    layout.addWidget(self.mass)
    layout.addWidget(self.molarWeight)
    layout.addWidget(self.concentration)
    layout.addWidget(self.volume)

    self.setLayout(layout)