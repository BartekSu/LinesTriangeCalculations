from PyQt5 import uic
from PyQt5.QtWidgets import QApplication  #pylint: disable=no-name-in-module, import error, bad-option-value
import math
import tkinter as tk
from tkinter import messagebox

cls, wnd = uic.loadUiType('program_Sura.ui')


class program_Sura(wnd, cls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def popup(self, title="", sentence=""):
        tk.Tk().withdraw()
        messagebox.showinfo(title=title, message=sentence)

    def on_RysujB1_pressed(self):
        if self.X1_1.text() == "" or self.X2_1.text() == "" or self.Y1_1.text() == "" or self.Y2_1.text() == "":
            self.popup("Błąd", "Wpisz liczby we wszytkie okienka")
        elif self.X1_1.text().isalpha() is True or self.X2_1.text().isalpha() is True or \
             self.Y1_1.text().isalpha() is True or self.Y2_1.text().isalpha() is True:
            self.popup("Błąd", "Wpisana wrtość nie jest liczbą")
        else:
            self.mpl.czysc()
            self.mpl.rysuj(float(self.X1_1.text()), float(self.X2_1.text()), float(self.Y1_1.text()),
                           float(self.Y2_1.text()))

    def on_RysujB2_pressed(self):
        if self.X1_2.text() == "" or self.X2_2.text() == "" or self.X3_2.text() == "" or self.Y1_2.text() == "" or \
           self.Y2_2.text() == "" or self.Y3_2.text() == "":
            self.popup("Błąd","Wpisz liczby we wszytkie okienka")
        elif self.X1_2.text().isalpha() is True or self.X2_2.text().isalpha() is True or \
             self.X3_2.text().isalpha() is True or self.Y1_2.text().isalpha() is True or \
             self.Y2_2.text().isalpha() is True or self.Y3_2.text().isalpha() is True:
            self.popup("Błąd", "Wpisana wrtość nie jest liczbą")
        else:
            self.mpl_2.czysc()
            self.mpl_2.rysuj_2(float(self.X1_2.text()), float(self.X2_2.text()), float(self.X3_2.text()),
                               float(self.Y1_2.text()), float(self.Y2_2.text()), float(self.Y3_2.text()))

    def on_ObliczB1_pressed(self):
        if self.X1_1.text() == "" or self.X2_1.text() == "" or self.Y1_1.text() == "" or self.Y2_1.text() == "":
            print("Wpisz liczby we wszytkie okienka")
        else:
            x = float(self.X2_1.text())-float(self.X1_1.text()) 
            y = float(self.Y2_1.text())-float(self.Y1_1.text()) 
            D = math.sqrt(pow(x, 2)+pow(y, 2))
            self.lEdx.setText(str(round(x, 2)))
            self.lEdy.setText(str(round(y, 2)))
            #self.wD.setText(str(f"{D:.2f}"))
            self.wD.setText(str(round(D, 2)))

    def on_ObliczB2_pressed(self):
        if self.X1_2.text() == "" or self.X2_2.text() == "" or self.X3_2.text() == "" or self.Y1_2.text() == "" or \
           self.Y2_2.text() == "" or self.Y3_2.text() == "":
            print("Wpisz liczby we wszytkie okienka")
        else:
            x12 = float(self.X2_2.text())-float(self.X1_2.text()) 
            y12 = float(self.Y2_2.text())-float(self.Y1_2.text()) 
            x23 = float(self.X3_2.text())-float(self.X2_2.text()) 
            y23 = float(self.Y3_2.text())-float(self.Y2_2.text()) 
            x31 = float(self.X1_2.text())-float(self.X3_2.text()) 
            y31 = float(self.Y1_2.text())-float(self.Y3_2.text()) 
            D12 = math.sqrt(pow(x12, 2)+pow(y12, 2))
            D23 = math.sqrt(pow(x23, 2)+pow(y23, 2))
            D31 = math.sqrt(pow(x31, 2)+pow(y31, 2))

            self.dL12.setText(str(round(D12, 2)))
            self.dL23.setText(str(round(D23, 2)))
            self.dL31.setText(str(round(D31, 2)))

            #Obliczenie pola za pomocą wzoru Herona
            p = (1/2)*(D12 + D23 + D31)
            pHeron = math.sqrt((p*(p-D12)*(p-D23)*(p-D31)))
            self.pL.setText(str(round(pHeron, 2)))
           
           
            #Obliczenie pola za pomocą tw sinusa
            p = math.acos((pow(D12, 2)+pow(D23, 2)-pow(D31, 2)) / (2*D12*D23))
            pSinus = (1/2)*D12*D23*math.sin(p)
            self.pL2.setText(str(round(pSinus, 2)))


    def on_CzyscB1_pressed(self):
        self.mpl.czysc()
        self.clear()    

    def on_CzyscB2_pressed(self):
        self.mpl_2.czysc()
        self.clear_2()    

    def on_LosujB1_pressed(self):
        self.X1_1.setText(str(round(self.mpl.losuj(), 2)))
        self.Y1_1.setText(str(round(self.mpl.losuj(), 2)))
        self.X2_1.setText(str(round(self.mpl.losuj(), 2)))
        self.Y2_1.setText(str(round(self.mpl.losuj(), 2)))

    def on_LosujB2_pressed(self):
        self.X1_2.setText(str(round(self.mpl.losuj(), 2)))
        self.Y1_2.setText(str(round(self.mpl.losuj(), 2)))
        self.X2_2.setText(str(round(self.mpl.losuj(), 2)))
        self.Y2_2.setText(str(round(self.mpl.losuj(), 2)))
        self.X3_2.setText(str(round(self.mpl.losuj(), 2)))
        self.Y3_2.setText(str(round(self.mpl.losuj(), 2)))

    def clear(self):
        self.X1_1.clear()
        self.X2_1.clear()
        self.Y1_1.clear()
        self.Y2_1.clear()
        self.lEdx.clear()
        self.lEdy.clear()
        self.wD.clear()

    def clear_2(self):
        self.X1_2.clear()
        self.X2_2.clear()
        self.Y1_2.clear()
        self.Y2_2.clear()
        self.X3_2.clear()
        self.Y3_2.clear()
        self.dL12.clear()
        self.dL23.clear()
        self.dL31.clear()
        self.pL.clear()
        self.pL2.clear()


app = QApplication([])
okno = program_Sura()
okno.show()
app.exec()
