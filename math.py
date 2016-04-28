Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1.0/2.0
0.5
>>> print "Hello,world!"
SyntaxError: Missing parentheses in call to 'print'
>>> print ("Hello,world!")
Hello,world!
>>> 1//2
0
>>> from _future_ import division
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    from _future_ import division
ImportError: No module named '_future_'
>>> from __future__ import division
>>> 1/2
0.5
>>> 10/3
3.3333333333333335
>>> 1//2
0
>>> 10%3
1
>>> 2**3
8
>>> 0xAF
175
>>> 010
SyntaxError: invalid token
>>> 0o10
8
>>> x=3
>>> x*2
6
>>> input("The meaning of life: ")
The meaning of life: 50
'50'
>>> x=input("x: ")
x: 30
>>> y=input("y: ")
y: 20
>>> print(x*y)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(x*y)
TypeError: can't multiply sequence by non-int of type 'str'
>>> print x*y
SyntaxError: Missing parentheses in call to 'print'
>>> x
'30'
>>> y
'20'
>>> int(x)
30
>>> int(y)
20
>>> print (x*y)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print (x*y)
TypeError: can't multiply sequence by non-int of type 'str'
>>> print(int(x)*int(y))
600
>>> pow(2,3)
8
>>> abs(-80)
80
>>> round(1.0/2.0)
0
>>> round(0.8)
1
>>> round(0.5)
0
>>> round(0.6)
1
>>> import math
>>> math.floor(15.4)
15
>>> int(math.floor(15.9))
15
>>> floor(15.5)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    floor(15.5)
NameError: name 'floor' is not defined
>>> from math import floor
>>> floor(15.5)
15
>>> 
