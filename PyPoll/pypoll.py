import csv 
import os

ballot_id=0
county=0
candidate=0
total_votes=0
complete_list=0

    #Make a dictionary 
thisdict = {
    "Charles Casper Stockham" : 0,
    "Diana DeGette" : 0,
    "Raymon Anthony Doane" : 0
    }



with open("C:/Users/salee/repos/python-challenge/PyPoll/Resources/election_data.csv",'r') as csv_file:

    #Define csv_reader
    csv_reader = csv.reader(csv_file) 
    header=next(csv_reader)

    for row in csv_reader:
        total_votes=total_votes+1
        complete_list= str(complete_list)+str(row[1])

        thisdict[row[2]] = thisdict[row[2]] + 1

dict_percent= {
    "Charles Casper Stockham" : (thisdict["Charles Casper Stockham"]/total_votes)*100,
    "Diana DeGette" : (thisdict["Diana DeGette"]/total_votes)*100,
    "Raymon Anthony Doane" : (thisdict["Raymon Anthony Doane"]/total_votes)*100
    }

max_candidate = ["",0]
for names, percentage in dict_percent.items():
    if max_candidate[1] < percentage:
        max_candidate[0] = names
        max_candidate[1] = percentage



output = f"""
  Election Results
  -------------------------
  Total Votes: {total_votes}
  -------------------------
  Charles Casper Stockham: { dict_percent ["Charles Casper Stockham"]:.3f}% ({thisdict['Charles Casper Stockham']})
  Diana DeGette: {dict_percent["Diana DeGette"]:.3f}% ({thisdict['Diana DeGette']})
  Raymon Anthony Doane: {dict_percent["Raymon Anthony Doane"]:.3f}% ({thisdict['Raymon Anthony Doane']})
  -------------------------
  Winner: {max_candidate[0]}
  -------------------------
"""
print(output)


with open("C:/Users/salee/repos/python-challenge/PyBank/Analysis/election_data.txt",'w') as out_file:
    out_file.write(output)

