from pathlib import Path
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class VentanaImagen(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("Visor de Recursos - Gestor de Torneos")
    self.resize(600, 400)
    self.setMinimumSize(400, 300)

    self.label_imagen = QLabel(self)
    self.label_imagen.setAlignment(Qt.AlignCenter)

    ruta_imagen = Path(r"C:\Users\alumno\Pictures\Screenshots\betis.png")

    if ruta_imagen.is_file():
      pixmap = QPixmap(str(ruta_imagen))

      pixmap_escalado = pixmap.scaled(
          400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation
      )
      self.label_imagen.setPixmap(pixmap_escalado)
    else:
      self.label_imagen.setText(
          f"No se encontró la imagen en:\n{ruta_imagen}"
      )

    self.setCentralWidget(self.label_imagen)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = VentanaImagen()
  ventana.show()
  sys.exit(app.exec())