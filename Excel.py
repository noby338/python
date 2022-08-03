import csv
def read_excel():
    excel = open('d:/null/charge2.CSV','r')
    reader = csv.DictReader(excel)
    for r in reader:
        print(r)

read_excel()