import sys
from PyQt5.QtWidgets import QApplication
from gui.hmac_window import FileHMACApp

def main():
    app = QApplication(sys.argv)
    window = FileHMACApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()