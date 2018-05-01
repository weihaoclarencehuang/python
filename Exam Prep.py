
#############################################################################################
# String and list slicing
#############################################################################################
s = "The number is 42."
print(s[4:-7])
print(s[-7:-1])
print(s[-6:len(s)])

>>>number
>>> is 42
>>>is 42.
#Note:
#if the start index is 0 then you can leave it blank
#if the end index is the length of the string then you can leave it blank

s = "The number is 42."
print(s[:5])
print(s[5:])
print(s[:])

>>>The n
>>>umber is 42.
>>>The number is 42.

s = "abcdef"
print(s[2::-1])
print(s[2:0:-1])
print(s[-4:-6:-1])

>>>cba
>>>cb
>>>cb

# Lower case
print("HELLO MR GUMBY".lower())
>>>hello mr gumby

my_jumble = ['jumbly', 'wumbly', 'number', 5]
print(my_jumble)
print(my_jumble[1])
print(my_jumble[-1])
print(my_jumble[:1:-1])

>>>['jumbly', 'wumbly', 'number', 5]
>>>wumbly
>>>5
>>>[5, 'number']


################################################################################
# List and range note
################################################################################
mylist[0:len(mylist)] # will return every element in mylist

>>> range(1,10) or range(10) # will return list below
[1, 2, 3, 4, 5, 6, 7, 8, 9]

#List and range together
mylist=[1,2,3,4,5]
for i in range(len(mylist)) # i will iterate every element in my list

################################################################################
# Counting using dictionary
################################################################################
MOBY = """Call me Ishmael. Some years ago"""

tally = {}
for char in MOBY:
    if char in tally:
        tally[char] += 1
    else:
        tally[char] = 1

print(tally['C'])
print(tally['I'])

# Result:
#      2
#      12

################################################################################
#  How to use Default dictionary
################################################################################
### Syntax begin
from collections import defaultdict
tally=defaultdict(list)

### Syntatx end

#Example

>>> from collections import defaultdict
# s is a list of tuples
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
        d[k].append(v)

>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

################################################################################
#  How to convert list back to string
################################################################################

list1 = ['1', '2', '3']
str1 = ''.join(list1)

################################################################################
#  Gnerate random number
################################################################################

import random
for i in range(20):
    print(random.randint(1,2))

random.uniform(0,1)

################################################################################
#  Recursive example
################################################################################

def mystery(x):
    if len(x)==1:
        return x[0]
    else:
        y=mystery(x[1:])
        if x[0]>y:
            return x[0]
        else:
            return y

x=[1,2,3]
mystery(x)

################################################################################
#  json
################################################################################
'''
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
'''

import json
x=json.loads('{"a":1,"1":"2"}')
type(x)  # dictionary
x        # {"a":1,"1":"2"}

y=json.loads("""["a","[","a","]"]""")
type(y) # list
y       # ['a', '[', 'a', ']']

x=json.loads("andrew") # return error message

################################################################################
#  string format
################################################################################

msg="SAYI Love ExamsEOM"
print("{}\n".format(msg[3:-3]))

################################################################################
#  class constructor format
################################################################################


class Ball:
    def __init__(self,radius='radius',color="red",position='position'):
        self.color=color
        self.radius=radius
        self.position=position

#If a keyword argument is put in, all arguments follow should be key arguments
x=Ball(position=2,color)
# This line will return error saying positional arguments
# follows keyword argument
x=Ball(radius=3,color='blue',position='US')
x.position      #Return 'US'
x.color         #Return blue
x=Ball(123,'red',5678)   # Initialise x variable rely on position argument
x.position      # Return 5678

################################################################################
#  class Example
################################################################################

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
