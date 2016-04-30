Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tag='<a href="http://www.python.org">Python web site</a>'
>>> tag[9:30]
'http://www.python.org'
>>> tag[32:-4]
'Python web site'
>>> numbers=[1,2,3,4,5,6,7,8,9,10]
>>> numbers[3:6]
[4, 5, 6]
>>> numbers[0:1]
[1]
>>> numbers[7:10]
[8, 9, 10]
>>> numbers[7:11]
[8, 9, 10]
>>> numbers[-3:-1]
[8, 9]
>>> numbers[-3:0]
[]
>>> numbers[-3:]
[8, 9, 10]
>>> numbers[1]
2
>>> numbers[:3]
[1, 2, 3]
>>> numbers[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> url=input('Please enter the URL: ')
Please enter the URL: http://www.python.com
>>> domain=url[11:-4]
>>> print('Domain name: '+domain)
Domain name: python
>>> numbers[0:10:1]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numbers[0:10:2]
[1, 3, 5, 7, 9]
>>> number[3:6:3]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    number[3:6:3]
NameError: name 'number' is not defined
>>> numbers[3:6:3]
[4]
>>> numbers[3:7:3]
[4, 7]
>>> numbers[::4]
[1, 5, 9]
>>> numbers[8:3:-1]
[9, 8, 7, 6, 5]
>>> numbers[10:0:-2]
[10, 8, 6, 4, 2]
>>> numbers[9:0:-2]
[10, 8, 6, 4, 2]
>>> numbers[0:10:-2]
[]
>>> numbers[::-2]
[10, 8, 6, 4, 2]
>>> numbers[5::-2]
[6, 4, 2]
>>> numbers[:5:-2]
[10, 8]
>>> numbers[:4:-2]
[10, 8, 6]
>>> 
