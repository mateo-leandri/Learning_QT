from UI_app import *

sum=0;


class MainWindow(QtWidgets.QWidget,Ui_Form):    #QtWidgets.QMainWindow para App tipo Window
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.ui=Ui_Form ()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.sumador)

    def sumador(self):
        global sum
        sum+=1
        self.ui.label_2.setText(str(sum))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()