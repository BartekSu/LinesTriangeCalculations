from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

#from random import random as rnd
import random

class MplCanvas1(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        super().__init__(Figure())
        self.setParent(parent)
        self.ax = self.figure.subplots()
        #print(self.ax)
        

    def rysuj(self, x1, x2, y1, y2):
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
    
        self.ax.plot([x1, x2],[y1,y2], c = color)
        self.ax.text(x1, y1, '1')
        self.ax.text(x2, y2, '2')
        self.draw()

    def rysuj_2(self, x1, x2, x3, y1, y2, y3):
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
    
        self.ax.plot([x1,x2,x3,x1],[y1,y2,y3,y1], c = color)
        self.ax.text(x1, y1, '1')
        self.ax.text(x2, y2, '2')
        self.ax.text(x3, y3, '3')
        self.draw()

        
    def losuj(self):
        x = random.uniform(0,100)
        return x


    def czysc(self):
        a = self.ax
        a.clear()
        self.draw()
'''
def rgb2gray(im):   
        r = im[:,:,0]
        g = im[:,:,1]
        b = im[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

        return gray
'''