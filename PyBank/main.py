import os
import csv
budget_data= os.path.join("Resources","budget_data.csv")
with open (budget_data, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvreader=next(csvfile)
def Totals (total_numbers):
    Months= str(total_numbers[0])
    profit_losses=int(total_numbers[1])
    Total_months= str(len(Months))
    Net_Total_Amount= int(len(profit_losses))
    print(Net_Total_Amount)
    print(Total_months)
#for Total_months in Months:
    #print(len(Total_months))

#def Average_changes (total_numbers):
    #Total_months= str(len(Months))
    #Net_Total_Amount=0
    #for number in profit_losses:
        #Net_Total_Amount+=number
        #return Net_Total_Amount/Total_months


