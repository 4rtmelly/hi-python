import json
import csv

def json2csv():
    data = json.load(open("exp.json"))

    recette = data['recette']
    outputfile = open('output.csv', 'w')
    csvWritter = csv.writer(outputfile)
    row = 0
    for clé in recette:
        if row == 0:
            header = clé.keys()
            csvWritter.writerow(header)
            row += 1
        csvWritter.writerow(clé.values())
        
    outputfile.close()

if __name__ == '__main__':
    json2csv()