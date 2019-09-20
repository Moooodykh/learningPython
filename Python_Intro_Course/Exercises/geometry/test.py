import polyplotter

def main():
    # Prepare the display object
    plotter = polyplotter.PolyPlotter()

    #large
    plotter.add_poly([ 0.51289531,  0.27156971],
                     [ 0.0019433,   0.95618624],
                     [ 0.25419353,  0.16787808])

    #medium
    plotter.add_poly([ 0.75772437,  0.99916542],
                     [ 0.12762848,  0.31368931],
                     [ 0.88809053,  0.97095824])

    #small
    plotter.add_poly([ 0.84896213,  0.65789054],
                     [ 0.86192205,  0.62178335],
                     [ 0.48373603,  0.76491545])

    # Draw polygons
    plotter.plot()

main()
