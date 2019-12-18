import csv

file = open("p024.txt", "w")
with open('test.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p026.txt", "w")
with open('test26.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p035.txt", "w")
with open('test35.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p039.txt", "w")
with open('test39.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p041.txt", "w")
with open('test41.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p042.txt", "w")
with open('test42.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p045.txt", "w")
with open('test45.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p047.txt", "w")
with open('test47.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
file = open("p049.txt", "w")
with open('test49.csv') as csvfile:
    readCsv = csv.reader(csvfile)
    for row in readCsv:
        ID = row[1]
        ID2 = row[2]
        file.write("/" + str(ID) + "/" + str(ID2) + "\n")
file.close()
