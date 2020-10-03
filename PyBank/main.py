import os
import csv
import statistics
def Totals(budget_data):
    profit_losses=[]
    date=[]
    total_months=0
    for row in budget_data:
        profit_losses.append(int(row[1]))
        date.append(str(row[0]))
        total_months+=1
        Net_Total=sum(profit_losses)
    Average_changes= float(statistics.mean(profit_losses))
    Rounded_Average_changes=round(Average_changes,2)
    max_increase= max(profit_losses)
    max_decrease= min(profit_losses)
    
    print(total_months)
    print(Net_Total)
    print(Rounded_Average_changes)
    print(max_increase)
    print(max_decrease)
    print(date[profit_losses.index(max_increase)+1])
    print(date[profit_losses.index(max_decrease)+1])

    Analysis = open("Analysis/Analysis.text", "w")
    Analysis.write(f"---Analysis Summary---\n"
    f"Total Months in budget data is {total_months}.\n"
    f"The net total amount of Profit/Losses is ${Net_Total}.\n" 
    f"The Average of the changes in Profit/Losses is:{Rounded_Average_changes}.\n"
    f"The greatest increase in profit occurred in {date[profit_losses.index(max_increase)+1]} (${max_increase}).\n" 
    f"The greatest decrease in losses occurred in {date[profit_losses.index(max_decrease)+1]} (${max_decrease}).\n")
    Analysis.close()
budget_data= os.path.join("Resources","budget_data.csv")

with open (budget_data, encoding='utf-8') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=",")
     header= next(csvreader)
     Totals(csvreader)