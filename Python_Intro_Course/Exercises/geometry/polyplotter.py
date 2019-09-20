import numpy
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import pylab

class PolyPlotter:

    patches = []

    def __init__(self):
        self.patches = []
        
        # colors
        cmap = matplotlib.pyplot.get_cmap('RdYlBu')
        num = [0, 0.35, 0.99] # 3 different colors
        self.colors = cmap(num)

    def add_poly(self, p1, p2, p3):
        poly = []
        poly.append(list(p1))
        poly.append(list(p2))
        poly.append(list(p3))
        
        pc = numpy.array(poly)
        polygon = Polygon(pc, True, color='g')
        self.patches.append(polygon)

    def selectColor(self,n):
        return self.colors[n]

    def clear(self):
        self.patches = []

    def plot(self):
        figure=pylab.figure()
        axes=figure.add_subplot(111)
        p = PatchCollection(self.patches, alpha=1)
        p.set_color(self.colors)
        axes.add_collection(p)
        pylab.show()
