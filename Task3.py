"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    #Declaring lists
    banglore_fixedline = []
    banglore_mobile = []
    banglore_tele = []
    
    #Separating out the numbers
    for number in calls:
      if number[0].startswith('(080)'):
        if(number[1].startswith('(')):
          prefix = number[1]
          prefix = prefix[prefix.find("(")+1:prefix.find(")")]
          banglore_fixedline.append(prefix)
        elif(number[1].startswith('140')):
          prefix = number[1][:2]
          banglore_tele.append(prefix)
        else:
          prefix = number[1][:3]
          banglore_mobile.append(prefix)


    final_set = set(banglore_fixedline + banglore_mobile +banglore_tele)
    print("The numbers called by people in banglore have codes : ")
    #Iterating to print numbers line by line
    for i in final_set:
      print(i)
    
    #Calculating % of people making calls in banglore from fixedline to fixedline
    per_fl_to_fl = round(len(banglore_fixedline)/len(banglore_fixedline+banglore_mobile+banglore_tele),2) * 100
    
    print(per_fl_to_fl,"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

    

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
