import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow


class VentanaNotificaciones(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("Notificaciones desactivadas")
    self.resize(400, 200)
    self.setMinimumSize(300, 150)

    self.checkbox = QCheckBox("Activar notificaciones", self)

    self.checkbox.setChecked(False)

    self.setCentralWidget(self.checkbox)

    self.checkbox.toggled.connect(self.cambiar_estado_notificaciones)

  @Slot(bool)
  def cambiar_estado_notificaciones(self, checked):
    """Actualiza el título de la ventana y registra el cambio en consola según el estado."""
    if checked:
      self.setWindowTitle("Notificaciones activadas")
      print("[CONSOLA] Notificaciones: ACTIVADAS")
    else:
      self.setWindowTitle("Notificaciones desactivadas")
      print("[CONSOLA] Notificaciones: DESACTIVADAS")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = VentanaNotificaciones()
  ventana.show()
  sys.exit(app.exec())