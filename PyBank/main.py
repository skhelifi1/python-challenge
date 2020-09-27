import os
import csv
budget_data.csv= os.path.join("..","Resources", "budget_data.csv")
with open (budget_data.csv, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
