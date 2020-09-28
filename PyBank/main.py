import os
import csv
budget_data= os.path.join("Resources","budget_data.csv")
with open (budget_data, encoding='utf-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvreader=next(csvfile)
def Totals (total_numbers):
         Months= str(total_numbers[0])
         profit_losses=int(total_numbers[1])
Totals(Months)
         
for Total_months in Months:
    print(len(Total_months))

Net_Total_Amount= int(len(profit_losses))

#def Average_changes (total_numbers):
    #length= len(Months)
    #total=0
    #for number in profit_losses:
        #total+=number
        #return total/length


