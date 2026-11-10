import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow


class VentanaProyecto(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("Proyecto sin nombre")
    self.resize(400, 200)
    self.setMinimumSize(300, 150)

    self.campo_texto = QLineEdit(self)

    self.campo_texto.setPlaceholderText("Introduce el nombre del proyecto...")

    self.campo_texto.setMaxLength(30)

    self.setCentralWidget(self.campo_texto)

    self.campo_texto.textChanged.connect(self.actualizar_titulo)

  @Slot(str)
  def actualizar_titulo(self, texto):
    """Actualiza el título de la ventana según el contenido del campo de texto."""
    if not texto or texto.isspace():
      self.setWindowTitle("Proyecto sin nombre")
    else:
      self.setWindowTitle(texto.upper())


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = VentanaProyecto()
  ventana.show()
  sys.exit(app.exec())