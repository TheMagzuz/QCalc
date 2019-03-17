from PyQt5.Qt import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class QDescriptionRow(QWidget): 
  def __init__(self, parent=None, flags=Qt.WindowFlags()):
    super().__init__(parent=parent, flags=flags)

    layout = QVBoxLayout()

    label = QLabel("Element")
    label.setStyleSheet("background-color: #FFFFFF")
    label.setFixedHeight(label.fontMetrics().height())

    #TODO: Fix aligment

    layout.addWidget(label)
    layout.addWidget(QLabel("x"))
    layout.addWidget(QLabel("n"))
    layout.addWidget(QLabel("m"))
    layout.addWidget(QLabel("Mw"))
    layout.addWidget(QLabel("C"))
    layout.addWidget(QLabel("V"))

    self.setLayout(layout)