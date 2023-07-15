# Write your code here
import argparse
import json
import re

terms = {}
mistakes = {}
loglist = []
parser = argparse.ArgumentParser()
parser.add_argument("--import_from")
parser.add_argument("--export_to")
args = parser.parse_args()

if args.import_from is not None:
    with open(args.import_from,'r') as data:
        # fa = data.readlines()
        fa = json.load(data)
        print(fa)
        for k, v in fa.items():
            terms[k] = v
        print(f'{len(terms)} cards have been loaded.')
        loglist.append(f'{len(terms)} cards have been loaded.')
else:
    pass

n = 0
while True:
    print('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
    term = input()
    loglist.append(term)
    if term == 'add':
        print('The card:')
        loglist.append('The card:')
        card = input()
        loglist.append(card)
        while True:
            if card in terms.keys():
                print(f'The card "{card}" already exists. Try again:')
                loglist.append((f'The card "{card}" already exists. Try again:'))
                card = input()
                loglist.append(card)
            else:
                print(f'The definition for card:')
                loglist.append((f'The definition for card:'))
                break
        defin = input()
        loglist.append(defin)
        while True:
            if defin in terms.values():
                print(f'The definition "{defin}" already exists. Try again:')
                loglist.append((f'The definition "{defin}" already exists. Try again:'))
                defin = input()
                loglist.append(defin)
            else:
                break
        terms[card] = defin
        print(f'The pair "{card}":"{defin}" has been added.')
        loglist.append(f'The pair "{card}":"{defin}" has been added.')
    if term == 'remove':
        print('Which card?')
        loglist.append('Which card?')
        card = input()
        loglist.append(card)
        if card in terms.keys():
            terms.pop(card)
            print('The card has been removed.')
            loglist.append('The card has been removed.')
        else:
            loglist.append(f'''Can't remove "{card}": there is no such card.''')
            print(f'''Can't remove "{card}": there is no such card.''')
    if term == 'exit':
        loglist.append('Bye bye!')
        print('Bye bye!')
        if args.export_to is not None:
            with open(args.export_to, 'w') as fileex:
                fileex.write(json.dumps(terms))
                # fileex.write(str(terms))
        print(f'{len(terms)} cards have been saved.')
        loglist.append(f'{len(terms)} cards have been saved.')
        break
    if term == 'export':
        print('File name:')
        loglist.append('File name:')
        filename = input()
        loglist.append(filename)
        with open(filename, 'w') as fileex:
            fileex.write(str(terms))
        print(f'{len(terms)} cards have been saved.')
        loglist.append(f'{len(terms)} cards have been saved.')
        # break
    if term == 'import':
        print('File name:')
        loglist.append('File name:')
        name = input()
        loglist.append(name)
        try:
            with open(name,'r') as failik:
                fa = failik.readlines()
                for i in fa:
                    terms.get(i)
                print(f'{len(terms)} cards have been loaded.')
                loglist.append(f'{len(terms)} cards have been loaded.')
        except FileNotFoundError:
            print('File not found')
            loglist.append('File not found')
    if term == 'ask':
        print('How many times to ask?')
        loglist.append('How many times to ask?')
        time = int(input())
        loglist.append(time)
        for i in range(time):
            print(f'Print the definition of "{list(terms.keys())}":')
            loglist.append(f'Print the definition of "{list(terms.keys())}":')
            res = input()
            loglist.append(res)
            if res == terms.values():
                print('Correct!')
                loglist.append('Correct!')
            else:
                loglist.append(n)
                if res in terms.values():
                    print(f'Wrong. The right answer is "{terms.values()}", but your definition is correct for "{list(terms.keys())[list(terms.values()).index(res)]}".')
                    loglist.append(f'Wrong. The right answer is "{terms.values()}", but your definition is correct for "{list(terms.keys())[list(terms.values()).index(res)]}".')
                else:
                    loglist.append(f'Wrong. The right answer is "{terms.values()}".')
                    print(f'Wrong. The right answer is "{terms.values()}".')
                n += 1
                mistakes[str(terms.keys())] = n
    if term == 'hardest card':
        if len(mistakes) == 0:
            print('There are no cards with errors.')
            loglist.append('There are no cards with errors.')
        else:
            print(f'The hardest card is {max(mistakes)}. You have {mistakes[max(mistakes)]} errors answering it.')
            loglist.append(f'The hardest card is {max(mistakes)}. You have {mistakes[max(mistakes)]} errors answering it.')
    if term == 'log':
        print('File name:')
        loglist.append('File name:')
        logname = input()
        # print(loglist)
        with open(logname, 'w') as logdoc:
            for i in loglist:
                logdoc.write(str(i))
        print('The log has been saved.')
    if term == 'reset stats':
        mistakes.clear()
        print('Card statistics have been reset.')
