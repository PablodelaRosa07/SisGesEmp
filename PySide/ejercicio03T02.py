import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class VentanaBienvenida(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("Gestor de Torneos - Bienvenida")
    self.resize(500, 300)
    self.setMinimumSize(400, 200)

    mensaje = (
        "¡Bienvenido al Sistema de Gestión de Torneos!\nOrganiza y compite"
        " fácilmente."
    )
    self.label = QLabel(mensaje, self)

    fuente = QFont()
    fuente.setPointSize(20)
    self.label.setFont(fuente)


    self.label.setAlignment(Qt.AlignCenter)
    self.label.setWordWrap(True)

    self.setCentralWidget(self.label)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = VentanaBienvenida()
  ventana.show()
  sys.exit(app.exec())