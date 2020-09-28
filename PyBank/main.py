import os
import csv
budget_data= os.path.join("Resources","budget_data.csv")
with open (budget_data, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvreader=next(csvfile)
       
Date=[]
profit_losses=[]

for Total_months in Date:
    print (Total_months)
