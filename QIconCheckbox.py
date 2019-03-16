from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui

class QIconCheckbox(QPushButton):
  

  def __init__(self, initialValue, *args, **kwargs):
    super(QIconCheckbox, self).__init__(*args, *kwargs)

    self.activeIcon = QtGui.QIcon('icons/locked-icon.png')
    self.inactiveIcon = QtGui.QIcon('icons/unlocked-icon.png')

    self.value = initialValue
    self.updateIcon()
    self.clicked.connect(self.updateValueAndIcon)

  def updateValueAndIcon(self):
    self.value = not self.value
    self.updateIcon()

    

  def updateIcon(self):
    if self.value:
      icon = self.activeIcon
    else:
      icon = self.inactiveIcon
    self.setIcon(icon)


