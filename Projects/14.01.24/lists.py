#Create a list and find out the min as well as the max
#Also Remove any duplicates
x = [2,4,8,2,1,35,7,8,2346,45]
min = min(x)
max = max(x)
y = list(dict.fromkeys(x))

print('list is ',end='')
for num in x:
    print(num,end=' ')
print()
print('min is ' + str(min))
print('max is ' + str(max))
print('without dup',end=' ')
for num in y:
    print(num,end=' ')

print('----------------------')

#Create a Dictionary(dict) containing information for a transaction
#Put multiple dict in a List so we can loop easy

transactions = [
    {'type':'sale', 'amount':50, 'date':'2024-01-14'},
    {'type':'sale', 'amount':50, 'date':'2024-01-14'},
    {'type':'purchase', 'amount':100, 'date':'2024-01-15'},
]

def listOf(myKey):
    x = [transaction[myKey] for transaction in transactions]
    return x
print(listOf('amount'))

def sumUp(myType):
    amountValues = [transaction['amount'] for transaction in transactions if transaction['type'] == myType]
    return(sum(amountValues))

def sumUpByDateHelper(type,key,date):
    x = [transaction['amount'] for transaction in transactions if transaction['type']==type and transaction[key]==date]
    return(x)

def sumUpByDate(key,date):
    x = sum(sumUpByDateHelper('sale',key,date))
    y = sum(sumUpByDateHelper('purchase',key,date))
    return(x-y)

print(sumUpByDate('date','2024-01-14'))

import re

pattern = r'^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$'

userDate = input('give me date     ')
if re.match(pattern,userDate):
    print('correct date')
else:
    print('no')
