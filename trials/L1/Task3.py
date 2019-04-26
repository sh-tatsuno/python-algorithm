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

def extract_prefix(phone):
  if phone[:3] == '140':
    return '140'
  for i in range(len(phone)):
    #if phone[0] == '(':
    if phone[i] == ')': 
      return phone[1:i]
    if phone[i] == ' ':
      return phone[:4]
  return -1

if __name__ == '__main__':
    dicts = {}
    for call in calls:
      prefix_caller = extract_prefix(call[0])
      if prefix_caller == '080':
        prefix = extract_prefix(call[1]) # receiver
        if prefix not in dicts:
          dicts[prefix] = 0
        dicts[prefix] += 1
    
    # PART A
    print("The numbers called by people in Bangalore have codes:")
    for line in sorted(list(dicts.keys())): print(line)

    # PART B
    print('{0:.2f}'.format(dicts['080'] / sum(dicts.values()) * 100), 'percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

