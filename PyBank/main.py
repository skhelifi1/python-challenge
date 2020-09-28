import os
import csv
budget_data= os.path.join("Resources","budget_data.csv")

Months=[]
profit_losses=[]
with open (budget_data, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    header=next(csvfile)
    for Months in csvreader:
        print (Months)

#def Totals (total_numbers):
    #Months= str(total_numbers[0])
    #profit_losses=int(total_numbers[1])
    #Total_months= str(len(Months))
    #Net_Total_Amount= int(len(profit_losses))
    #print(Net_Total_Amount)
    #print(Total_months)

#for row in csvreader:
    #print(row)

#def Average_changes (total_numbers):
    #Total_months= str(len(Months))
    #Net_Total_Amount=0
    #for number in profit_losses:
        #Net_Total_Amount+=number
        #return Net_Total_Amount/Total_months


