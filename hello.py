Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name=raw_input("What is your name?")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name=raw_input("What is your name?")
NameError: name 'raw_input' is not defined
>>> name=input("What is your name?")
What is your name?wk
>>> print ("Hello,"+name+"!")
Hello,wk!
>>> 
