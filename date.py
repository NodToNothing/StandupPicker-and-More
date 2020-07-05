import datetime, calendar
year = 2020
month = 7
num_days = calendar.monthrange(year, month)[1]
print("<ol>")
for i in range(num_days, 0, -1):
    print("<li>" + str(month) + "/" + str(i) + "/" + str(year) + ": </li>")
print("</ol>")
