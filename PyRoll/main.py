#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.

import csv
import os

#define file path
path = os.path.join("..", "Resources", "election_data.csv")

#open the election data
with open(path, newline="") as election_raw:
    #read in the csv
    election = csv.reader(election_raw, delimiter = ",")
    #define file headers
    headers = next(election, None)
    #convert to a list
    election = list(election)
    
    #find and print total votes cast
    total_votes = len(election)
    #print(total_votes)

    #create empty dictionary to hold election results
    results = {}

    #loop through results to populate dictionary with candidates and vote totals
    for row in election:
        if row[2] in results:
            results[row[2]] +=1
        else:
            results[row[2]] = 1
    
    #calculate percentages
    #create empty list
    perc = []
    #loop through results to calculate percentages and save to list
    for i in results:
        perc.append(str(round(results[i]/total_votes,4)*100) + "%")


    #extract keys and values from dictionary to separate lists
    candidates = results.keys()
    votes = results.values()
    #combine candidates, votes and percentages into single item
    output = zip(candidates,votes,perc)
    #turn output to a set
    output = set(output)
    
    

    #calculate winner
    winner = max(results, key=results.get)

    #print results
    print(f'Election Results \n Total Votes: {total_votes} \n {output} \n Winner: {winner}')

    #print out and save results to a text file
    text_output = open('PyPoll_Results.txt','w')
    text_output.write('Election Results \n Total Votes: ' + repr(total_votes) + '\n' + repr(output) + '\n Winner: ' + repr(winner))
    text_output.close()