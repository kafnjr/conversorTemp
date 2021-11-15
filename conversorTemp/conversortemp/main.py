from conversortemp import conversor
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = conversor.Ui_conversor()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
