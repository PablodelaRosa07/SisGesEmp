import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class VentanaBotonPresionado(QMainWindow):

  def __init__(self):
    super().__init__()

    # Configuramos la ventana
    self.setWindowTitle("Control de Pulsación")
    self.resize(400, 250)
    self.setMinimumSize(300, 200)

    # Creamos el botón con el texto inicial "Pulsar"
    self.boton = QPushButton("Pulsar", self)

    # 5. El botón no es conmutable por defecto (setCheckable es False)
    self.boton.setCheckable(False)

    # Establecemos el botón como widget central
    self.setCentralWidget(self.boton)

    # Conectamos las señales 'pressed' y 'released' a métodos diferentes
    self.boton.pressed.connect(self.al_presionar)
    self.boton.released.connect(self.al_liberar)

  def al_presionar(self):
    """Se ejecuta mientras el botón está presionado."""
    # 1. Cambiar el texto a «Soltar»
    self.boton.setText("Soltar")
    # 3. Mostrar en consola «Botón presionado»
    print("Botón presionado")

  def al_liberar(self):
    """Se ejecuta cuando se libera el botón."""
    # 2. Recuperar el texto «Pulsar»
    self.boton.setText("Pulsar")
    # 4. Mostrar en consola «Botón liberado»
    print("Botón liberado")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = VentanaBotonPresionado()
  ventana.show()
  sys.exit(app.exec())