"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    #Create a new list to save values
    mobile_number_text = []
    
    #iterate throught the list to get the numbers
    for mob_no_text in texts:
        mobile_number_text.append(mob_no_text[0])
        mobile_number_text.append(mob_no_text[1])
    #Gives unique mobile number
    unique_mobile_number_text = len(set(mobile_number_text))
    

            

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
    #Create a new list to save values
    mobile_number_call=[]
    
    #iterate throught the list to get the numbers
    for mob_no_call in calls:
        mobile_number_call.append(mob_no_call[1])
        mobile_number_call.append(mob_no_call[0])
        
    #Gives unique mobile number
    unique_mobile_number_call = len(set(mobile_number_call))
    

total_unique_number = unique_mobile_number_call + unique_mobile_number_text
print("There are ",total_unique_number," different telephone numbers in the records.")



"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
