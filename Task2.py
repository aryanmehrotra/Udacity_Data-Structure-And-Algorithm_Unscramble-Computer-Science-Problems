"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    #Creating Dictionary
    num_time={}

    #iterating with if else conditons to get insert details in dictionary (num_time)
    for data in calls:
        if data[0] in num_time:
            num_time[data[0]] = int(num_time[data[0]])+int(data[3])
        else:
            num_time[data[0]] = data[3]
    for key in num_time:
        num_time[key] = int(num_time[key]) 
    
    #To get max value and key from the dictionary
    max_value = max(num_time.values())
    max_key = max(num_time, key=num_time.get)
    
    print(max_key," spent the longest time, " ,max_value," seconds, on the phone during September 2016.")

    
    




"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

