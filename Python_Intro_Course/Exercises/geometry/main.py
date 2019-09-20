import polyplotter

def main():
    # Prepare the display object
    plotter = polyplotter.PolyPlotter()


    # Read and parse the points from the input file
    # Build the list of polygons, sorted in z-order   
csvFile = open('polygons.txt', 'r')
csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')

# Read the txt file into a list of rows
ratings = []
for row in csvReader:
    ratings.append(row)
print(ratings[0])
inputArray = ratings[0]
#NumList = [float(x) for x in inputArray]

inputArray.Split()

    # Draw polygons
#    plotter.plot()

main()

