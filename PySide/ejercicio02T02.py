import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class VentanaInterruptor(QMainWindow):

  def __init__(self):
    super().__init__()

    # 3. Mostrar inicialmente la funcionalidad como desactivada
    self.setWindowTitle("Sistema de Vigilancia - Desactivado")
    self.resize(400, 250)
    self.setMinimumSize(300, 200)

    # 2. Incorporar un botón conmutable mediante setCheckable(True)
    self.boton = QPushButton("Activar Sistema")
    self.boton.setCheckable(True)

    # Establecer el botón como widget central
    self.setCentralWidget(self.boton)

    # 5. Utilizar clicked para registrar las activaciones en consola
    self.boton.clicked.connect(self.registrar_clic)

    # 6. Utilizar toggled para actualizar la interfaz
    self.boton.toggled.connect(self.actualizar_estado)

  # 8. Utilizar @Slot(bool) en los métodos receptores
  @Slot(bool)
  def registrar_clic(self, checked):
    """Registra en consola cada vez que el usuario hace clic en el botón."""
    estado = "ACTIVADO" if checked else "DESACTIVADO"
    print(f"[CONSOLA] Acción de clic registrada. Estado actual: {estado}")

  @Slot(bool)
  def actualizar_estado(self, checked):
    """Actualiza la interfaz de la ventana y el texto del botón según el estado."""
    if checked:
      self.setWindowTitle("Sistema de Vigilancia - Activo")
      self.boton.setText("Desactivar Sistema")
    else:
      self.setWindowTitle("Sistema de Vigilancia - Desactivado")
      self.boton.setText("Activar Sistema")


if __name__ == "__main__":
  # 1. Crear la instancia de la aplicación y la ventana
  app = QApplication(sys.argv)
  ventana = VentanaInterruptor()
  ventana.show()
  sys.exit(app.exec())