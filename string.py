Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #get user name
>>> user_name=input("what is your name?")
what is your name?wangkang
>>> print(user_name)
wangkang
>>> "Hello,"+"world!"
'Hello,world!'
>>> x="Hello,"
>>> y="world!"
>>> x+y
'Hello,world!'
>>> "Hello,world!"
'Hello,world!'
>>> 10000L
SyntaxError: invalid syntax
>>> 10000
10000
>>> print ("Hello,world!")
Hello,world!
>>> temp=40
>>> print ("the temperature is "+temp)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print ("the temperature is "+temp)
TypeError: Can't convert 'int' object to str implicitly
>>> print ("the temperature is "+`temp`)
SyntaxError: invalid syntax
>>> print ("the temperature is "+repr(temp))
the temperature is 40
>>> print '''this is a very long string.'''
SyntaxError: Missing parentheses in call to 'print'
>>> print ('''this is a very long string.''')
this is a very long string.
>>> print('Hello.\nworld!')
Hello.
world!
>>> print ("c:\nowhere")
c:
owhere
>>> print ("c:\\nowhere")
c:\nowhere
>>> print (r"c:\nowhere")
c:\nowhere
>>> print ("c:\nowhere\")
       
SyntaxError: EOL while scanning string literal
>>> print ("c:\nowhere"+"\\")
c:
owhere\
>>> print (r"c:\nowhere"+"\\")
c:\nowhere\
>>> print ("你好，世界")
你好，世界
>>> print (u"hello,world!")
hello,world!
>>> 
