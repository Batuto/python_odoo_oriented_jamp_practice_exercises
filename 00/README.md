You must implement an application that require multiple date formats to
be transformed into one common date format.

Task:
Implement a function named change_date_format which may accept a list of strings. These strings represents dates, and the function should return a new list with each date in the following format: YYYYMMDD
Only the dates incoming with the following formats will be valid and should be 
returned.
 - YYYY/MM/DD
 - DD/MM/YYYY
 - MM-DD-YYYY

(All of YY, MM and DD are only numbers representing Year, Month and Day)

For example, change_date_format(["2013/08/21", "18/12/2020", "12-04-2009",
"20130720"]) should return the list ["20130821", "20201218", "20091204"].

