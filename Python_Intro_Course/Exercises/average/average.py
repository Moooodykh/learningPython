import csv

# Open the csv and create a reader object
csvFile = open('ratings.csv', 'r')
csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')

# Read the csv file into a list of rows
ratings = []
for row in csvReader:
    ratings.append(row)
#Numberavergae = Numbersum / len(ratings) 
# Print the first row
print(ratings[0])


NumList = ratings[0]
NumList = [float(x) for x in NumList]
        #map(float,Numlist)

Listsum = sum(NumList)
average = Listsum / len(NumList)

print('Sum =', Listsum)
print('Average =', average)


