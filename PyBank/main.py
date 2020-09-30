import os
import csv
import statistics
def Totals(budget_data):
    profit_losses=[]
    total_months=0
    for row in budget_data:
        profit_losses.append(int(row[1]))
        total_months+=1
        Net_Total=sum(profit_losses)
    Average_changes= float(statistics.mean(profit_losses))
    max_increase= max(profit_losses)
    max_decrease= min(profit_losses)
    print (total_months)
    print (Net_Total)
    print(Average_changes)
    print(max_increase)
    print(max_decrease)
    date=[]    
    for row in budget_data:
        date.append(str(row[0]))
        if row == max_increase:
            print (date)
        elif row == max_decrease:
            print (date)
budget_data= os.path.join("Resources","budget_data.csv")

with open (budget_data, encoding='utf-8') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=",")
     header= next(csvreader)
     Totals(csvreader)

# Analysis = open("Analysis/Analysis.text", "w")
# Analysis.write(f"---Analysis Summary---"
# "Total Months in budget data is:{total_months}\n" 
# "The net total amount of Profit/Losses is:{Net_Total}.\n" 
# "The Average of the changes in Profit/Losses is {Average_changes}.]\n"
# "The greates increase in profit is {max_increase}.\n" 
# "The greatest decrease in losses is{max_decrease}.\n"
#  textfile.close()