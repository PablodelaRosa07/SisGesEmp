import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit


class EditorNotas(QMainWindow):

  def __init__(self):
    super().__init__()

    self.setWindowTitle("Editor de notas — 0 caracteres")
    self.resize(600, 400)
    self.setMinimumSize(400, 300)

    self.editor = QTextEdit(self)

    self.editor.setPlaceholderText("Escribe aquí tus notas")

    self.editor.setAcceptRichText(False)

    self.setCentralWidget(self.editor)

    self.editor.textChanged.connect(self.actualizar_contador)

  @Slot()
  def actualizar_contador(self):
    """Actualiza el título de la ventana con el número de caracteres y palabras."""
    texto = self.editor.toPlainText()

    num_caracteres = len(texto)

    palabras = texto.split()
    num_palabras = len(palabras)

    if num_caracteres == 0:
      self.setWindowTitle("Editor de notas — 0 caracteres")
    else:
      self.setWindowTitle(
          f"Editor de notas — {num_caracteres} caracteres — {num_palabras}"
          f" palabras"
      )


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = EditorNotas()
  ventana.show()
  sys.exit(app.exec())