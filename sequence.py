Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> 'Hello,'+'world!'
'Hello,world!'
>>> [1,2,3]+'world!'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    [1,2,3]+'world!'
TypeError: can only concatenate list (not "str") to list
>>> 'python'*5
'pythonpythonpythonpythonpython'
>>> [42]*10
[42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
>>> sequence=[None]*10
>>> sequence
[None, None, None, None, None, None, None, None, None, None]
>>> sentence=input('Sentence: ');
Sentence: he is a very naughty boy!
>>> 
>>> screen_width=80
>>> text_width=len(sentence)
>>> box_width=text_width+6
>>> left_margin=(scren_width-box_width)//2
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    left_margin=(scren_width-box_width)//2
NameError: name 'scren_width' is not defined
>>> left_margin=(screen_width-box_width)//2
>>> 
>>> print();

>>> print ' '*left_margin+'+'+'-'*(box_width-2)+'+'
SyntaxError: invalid syntax
>>> print (' '*left_margin+'+'+'-'*(box_width-2)+'+')
                        +-----------------------------+
>>> print (' '*left_margin+'|'+' '*(box_width-2)+'|')
                        |                             |
>>> print (' '*left_margin+'|'+sentence+'|')
                        |he is a very naughty boy!|
>>> print (' '*left_margin+'|'+' '*(box_width-2)+'|')
                        |                             |
>>> print (' '*left_margin+'+'+'-'*(box_width-2)+'+')
                        +-----------------------------+
>>> permissions='rw'
>>> 'w' in permissions
True
>>> 'x' in permissions
False
>>> user=['mlh','foo','bar']
>>> input('Enter your user name: ') in user
Enter your user name: foo
True
>>> subject='$$$Get rich now!!!$$$'
>>> '$$$' in subject
True
>>> database=[['albert','1234'],['dilbert','4242'],['smith','7524'],['jones','9843']]
>>> username=input('user name: ')
user name: albert
>>> pin=input('pin code: ')
pin code: 1234
>>> if[username,pin] in database:print 'Access granted'
SyntaxError: Missing parentheses in call to 'print'
>>> if[username,pin] in database:print('Access granted')

Access granted
>>> numbers=[100,34,678]
>>> len(numbers)
3
>>> max(numbers)
678
>>> min(numbers)
34
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> x=[1,1,1]
>>> x[1]=2
>>> x
[1, 2, 1]
>>> names=['Alice','Beth','Cecil','Dee-Dee','Earl']
>>> del names[2]
>>> names
['Alice', 'Beth', 'Dee-Dee', 'Earl']
>>> name=list('Perl')
>>> name
['P', 'e', 'r', 'l']
>>> name[2:]=list('ar')
>>> name
['P', 'e', 'a', 'r']
>>> name=list('Perl')
>>> name[1:]=list('ython')
>>> name
['P', 'y', 't', 'h', 'o', 'n']
>>> numbers=[1,5]
>>> numbers[1:1]=[2,3,4]
>>> numbers
[1, 2, 3, 4, 5]
>>> numbers=[1,5]
>>> numbers[1:2]=[2,3,4]
>>> numbers
[1, 2, 3, 4]
>>> numbers=[1,2,3,4,5]
>>> numbers[1,4]=[]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    numbers[1,4]=[]
TypeError: list indices must be integers, not tuple
>>> numbers[1:4]=[]
>>> numbers
[1, 5]
>>> lst=[1,2,3]
>>> lst.append(4)
>>> lst
[1, 2, 3, 4]
>>> ['to','be','or','not','to','be'].count('to')
2
>>> x=[[1,2],1,1,[2,1,[1,2]]]
>>> x.count(1)
2
>>> x.count([1,2])
1
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a
[1, 2, 3]
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> a[len(a):]=b
>>> a
[1, 2, 3, 4, 5, 6]
>>> knights=['We','are','the','knights','who','say','ni']
>>> knights.index('who')
4
>>> knights[4]
'who'
>>> numbers=[1,2,3,5,6,7]
>>> numbers.insert(3,'four')
>>> numbers
[1, 2, 3, 'four', 5, 6, 7]
>>> x=[1,2,3]
>>> x.pop()
3
>>> x
[1, 2]
>>> x.pop(0)
1
>>> x
[2]
>>> x=[1,2,3]
>>> x.append(x.pop)
>>> x
[1, 2, 3, <built-in method pop of list object at 0x021935A8>]
>>> x.append(x.pop())
>>> x
[1, 2, 3, <built-in method pop of list object at 0x021935A8>]
>>> x=[1,2,3]
>>> x.append(x.pop())
>>> x
[1, 2, 3]
>>> x=['to','be','or','not','to','be']
>>> x.remove('be')
>>> x
['to', 'or', 'not', 'to', 'be']
>>> x=[1,2,3]
>>> x.reverse()
>>> x
[3, 2, 1]
>>> x=[4,6,2,1,7,9]
>>> x.sort()
>>> x
[1, 2, 4, 6, 7, 9]
>>> x=[4,6,2,1,7,9]
>>> y=x.sort()
>>> print(y)
None
>>> x=[4,6,2,1,7,9]
>>> y=x[:]
>>> y.sort()
>>> x
[4, 6, 2, 1, 7, 9]
>>> y
[1, 2, 4, 6, 7, 9]
>>> x=[4,6,2,1,7,9]
>>> y=sorted(x)
>>> x
[4, 6, 2, 1, 7, 9]
>>> y
[1, 2, 4, 6, 7, 9]
>>> sorted('Python')
['P', 'h', 'n', 'o', 't', 'y']
>>> cmp(4,3)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    cmp(4,3)
NameError: name 'cmp' is not defined
>>> x=['aardvark','abalone','acme','add','aerate']
>>> x.sort(key=len)
>>> x
['add', 'acme', 'aerate', 'abalone', 'aardvark']
>>> x=[4,6,2,1,7,9]
>>> x.sort(reverse=True)
>>> x
[9, 7, 6, 4, 2, 1]
>>> 
