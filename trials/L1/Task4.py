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

if __name__ == '__main__':
    all_phones = set()
    receive_or_use_text_phones = set()
    for text in texts:
        all_phones.add(text[0]) 
        all_phones.add(text[1])
        receive_or_use_text_phones.add(text[0])
        receive_or_use_text_phones.add(text[1])

    for call in calls:
        all_phones.add(call[0])
        all_phones.add(call[1])
        # receive_or_use_text_phones.add(call[0]) #sender
        receive_or_use_text_phones.add(call[1])

    print("These numbers could be telemarketers:")
    results = sorted(list(all_phones - receive_or_use_text_phones))
    for line in results: print(line)
