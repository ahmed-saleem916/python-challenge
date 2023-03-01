import csv 
import os 

total_month=0
total_net=0
pre_net=0
total_change=0
change_counter=0
greatest_decrease=0
greatest_increase=0
greatest_dedate=""
greatest_indate=""
change=0

#copy as path 
with open("C:/Users/salee/repos/python-challenge/PyBank/Resources/budget_data.csv",'r') as csv_file:
    
    #define csv reader
    csv_reader = csv.reader(csv_file) 
    header=next(csv_reader)
   
    
    for row in csv_reader:
        total_month=total_month + 1
        total_net=total_net + int(row[1])
        current_net=int(row[1])

        if pre_net!=0:
            change=current_net-pre_net
            total_change=total_change+change
            change_counter=change_counter+1

        if change > greatest_increase:
            greatest_increase=change
            greatest_indate=row[0]
        
        if change < greatest_decrease:
            greatest_decrease=change 
            greatest_dedate=row[0]



        pre_net=int(row[1])

average_change=round(total_change/change_counter,2)
print(greatest_increase)
print(greatest_indate)
print(greatest_dedate)
print(greatest_decrease)



output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_net}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_indate} (${greatest_increase})
Greatest Decrease in Profits: {greatest_dedate} (${greatest_decrease})
"""

print(output)

with open("Analysis/budget_output.txt",'w') as out_file:
    out_file.write(output)