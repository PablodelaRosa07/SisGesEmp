from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow
import sys


class VentanaNotificacionesTristate(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Notificaciones: Desactivadas")
    self.resize(400, 200)

    self.checkbox = QCheckBox("Activar notificaciones", self)
    self.checkbox.setTristate(True)
    self.setCentralWidget(self.checkbox)

    self.checkbox.checkStateChanged.connect(self.cambiar_estado_tristate)

  @Slot(Qt.CheckState)
  def cambiar_estado_tristate(self, state):
    if state == Qt.Checked:
      self.setWindowTitle("Notificaciones: Activadas")
      print("[CONSOLA] Estado: Activado")
    elif state == Qt.PartiallyChecked:
      self.setWindowTitle("Notificaciones: Parciales / Silenciadas")
      print("[CONSOLA] Estado: Parcial (Silenciadas)")
    else:  
      self.setWindowTitle("Notificaciones: Desactivadas")
      print("[CONSOLA] Estado: Desactivado")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = VentanaNotificacionesTristate()
  ventana.show()
  sys.exit(app.exec())