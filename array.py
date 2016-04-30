Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> edward=['Edward Gumby',42]
>>> john=['John Smith',50]
>>> database=[edward,john]
>>> database
[['Edward Gumby', 42], ['John Smith', 50]]
>>> greeting='Hello'
>>> greeting[0]
'H'
>>> greeting[-1]
'o'
>>> 'Hello'[1]
'e'
>>> fourth=input('Year: ')[3]
Year: 2016
>>> fourth
'6'
>>> months=['January','February','March','April','May','June','July','August','September','October','November','December']
>>> endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
>>> year=input('Year: ')
Year: 2016
>>> month=input('Month(1-12): ')
Month(1-12): 4
>>> day=input('Day(1-31): ')
Day(1-31): 29
>>> month_number=int(month)
>>> day_number=int(day)
>>> month_name=months[month_number-1]
>>> ordinal=day+endings[day_number-1]
>>> 
>>> print(month_name+' '+ordinal+', '+year)
April 29th, 2016
>>> 
