"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    #Declaring Lists

    #Sent sms
    numbers_text_send = []

    #Received Sms
    numbers_text_receive = []

    #Iterating to separate numbers
    for number_text in texts:
        numbers_text_send.append(number_text[0])
        numbers_text_receive.append(number_text[1])



with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    #Declaring Lists 

    #Outgoing Calls
    numbers_call_out = []

    #Incoming Calls
    numbers_call_in = [] 

    #Iterating to separate numbers
    for number_call in calls:
        numbers_call_out.append(number_call[0])
        numbers_call_in.append(number_call[1])
    
    combined = set(numbers_text_send+numbers_text_receive+numbers_call_in)
    numbers_call_out = set(numbers_call_out)
    
    telemarketers = numbers_call_out - combined
    print("These numbers could be telemarketers:")
    for i in telemarketers:
        print(i)



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

