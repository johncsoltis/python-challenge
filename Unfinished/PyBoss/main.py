#Import the employee_data.csv file, which currently holds employee records
#Then convert and export the data to use the following format instead:
    #Emp ID,First Name,Last Name,DOB,SSN,State
    #214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#In summary, the required conversions are as follows:
    #The Name column should be split into separate First Name and Last Name columns.
    #The DOB data should be re-written into MM/DD/YYYY format.
    #The SSN data should be re-written such that the first five numbers are hidden from view.
    #The State data should be re-written as simple two-letter abbreviations.

#import csv and os modules
import csv
import os

#define file path
path = os.path.join("..", "Resources","employee_data.csv")

#create empty lists for new fields
emp_id = []
name = []
birth = []
ssn = []
state = []


#open data
with open(path, newline="") as employee_raw:
    #read csv
    employees = csv.reader(employee_raw, delimiter=",")
    #define headers
    headers = next(employees)
    #populate destination lists
    for row in employees:
        emp_id.append(row[0])
        name.append(row[1])
        birth.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
    
    #separate first and last names
    first = []
    last = []
    for i in name:
        #split name using a blank space as a delimiter
        splitter = i.split(" ")
        #append the split names to new lists
        first.append(splitter[0])
        last.append(splitter[1])

    #change ssn format
    for i in ssn:


    #change state so abbreviaions
    state_abr = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
