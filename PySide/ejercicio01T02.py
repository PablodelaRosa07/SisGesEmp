import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# PARTE A: Ejemplo inicial modificado

class Ventana(QMainWindow):

  def __init__(self):
    super().__init__()

    # 1. Cambiamos el título de la ventana por el nombre de la aplicación
    self.setWindowTitle("Gestor de Torneos")

    # 2. Establecemos un tamaño inicial de 600 x 350
    self.resize(600, 350)

    # 3. Configuramos un tamaño mínimo de 400 x 250
    self.setMinimumSize(400, 250)

    # 4. Modificamos el texto del botón con una acción relacionada
    self.boton = QPushButton("Crear nuevo torneo")

    # Colocamos el botón en el centro de la ventana
    self.setCentralWidget(self.boton)


# PARTE C: Segunda ventana (VentanaAlternativa)

class VentanaAlternativa(QMainWindow):

  def __init__(self):
    super().__init__()

    # 4. Establecemos un título diferente al de la parte A
    self.setWindowTitle("Control de Partidas y Jugadores")

    # 5. Tamaño inicial de 500 x 300 y tamaño mínimo de 350 x 200
    self.resize(500, 300)
    self.setMinimumSize(350, 200)

    # 6. Creamos un botón con texto de acción para esta segunda app
    self.boton = QPushButton("Registrar resultado")

    # 7. Establecemos el botón como widget central
    self.setCentralWidget(self.boton)


# Bloque Principal de Ejecución

if __name__ == "__main__":
  # 8. Crear la instancia de QApplication
  app = QApplication(sys.argv)

  # Cambiar entre Ventana() o VentanaAlternativa() según lo que desee probar
  ventana = Ventana()
  # ventana = VentanaAlternativa()

  # Mostrar la ventana seleccionada e iniciar el bucle de eventos
  ventana.show()
  sys.exit(app.exec())