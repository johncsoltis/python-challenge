#Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

#import the csv modulde
import csv
import os

#define file path
path = os.path.join("..", "Resources", "budget_data.csv")

#set empty variables
total_months = 0
total_revenue = 0
prev_revenue = 0
new_revenue =0
max_change = ["",0]
min_change = ["",0]
changes = []

#open csv
with open(path, newline="") as csv_budget:
    #read csv
    budget = csv.reader(csv_budget)
    header = next(budget)
    #run for loop to calculate total months and total revenue
    for row in budget:
        total_months += 1
        total_revenue = total_revenue + int(row[1])

        new_revenue = int(row[1])
        difference = prev_revenue - new_revenue
        changes.append(difference)
        prev_revenue = new_revenue
        #use if statements to populate max and min changes
        if difference >= int(max_change[1]):
            max_change = row
        if difference <= int(min_change[1]):
            min_change = row

    print(f'This dataset contains {total_months} months')
    print(f'The total revenue over all periods is ${total_revenue}')

    #find the difference between each period and add the 'changes' list
    #for row in budget:


    #find the average change
    average = sum(changes)/total_months

    print(f'The average change between periods is {average}')
    print(f'Max change: {max_change}')
    print(f'Min change: {min_change}')