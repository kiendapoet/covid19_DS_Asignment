# read file
with open("vietnam.csv") as file:
	data = file.read().split("\n")

header = data[0]
lines = data[1:]

# remove last student (empty student)
lines.pop()

dates = []
new_case = []
for i in range(len(lines)):
	lines[i] = lines[i].split(",")
	dates.append(lines[i][0])
	new_case.append(int(lines[i][4]))
# 	lines[i][0] = lines[i][0].split("/")

# total_cases_per_month = [0,0,0,0,0,0,0,0,0,0,0,0]


# for line in lines:
# 	if line[0][2] == "2020":
# 		if line[0][0] == "1":
# 			total_cases_per_month[0] += int(line[2])
# 		if line[0][0] == "2":
# 			total_cases_per_month[1] += int(line[2])
# 		if line[0][0] == "3":
# 			total_cases_per_month[2] += int(line[2])
# 		if line[0][0] == "4":
# 			total_cases_per_month[3] += int(line[2])
# 		if line[0][0] == "5":
# 			total_cases_per_month[4] += int(line[2])
# 		if line[0][0] == "6":
# 			total_cases_per_month[5] += int(line[2])
# 		if line[0][0] == "7":
# 			total_cases_per_month[6] += int(line[2])
# 		if line[0][0] == "8":
# 			total_cases_per_month[7] += int(line[2])
# 		if line[0][0] == "9":
# 			total_cases_per_month[8] += int(line[2])
# 		if line[0][0] == "10":
# 			total_cases_per_month[9] += int(line[2])
# 		if line[0][0] == "11":
# 			total_cases_per_month[10] += int(line[2])
# 		if line[0][0] == "12":
# 			total_cases_per_month[11] += int(line[2])

# # define months:
# months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aus","Sep","Oct","Nov","Dec"]

# # plot barchart
# # https://pythonspot.com/matplotlib-bar-chart/
# import matplotlib.pyplot as plt
# import numpy 

# figure, axis = plt.subplots()

# # list from 0-11 : 12 months instead
# y_pos = numpy.arange(12)

# # plot the barchart using 2 list
# plt.bar(y_pos, total_cases_per_month)

# # change horizontal category name
# plt.xticks(y_pos, months)

# # set limit to vertical axis
# axis.set_ylim(0,600)

# # label and title
# plt.ylabel('The total cases')
# plt.title('The total cases of Covid-19 per month in Vietnam in 2020')

# # Draw number of student on top of each bar
# # https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
# rects = axis.patches
# for rect, label in zip(rects, total_cases_per_month):
#     height = rect.get_height()
#     axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label, ha='center', va='bottom')

# # show the plot
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
figure, axis = plt.subplots()

x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

y = new_case
# axis.set_ylim(0,600)
plt.ylabel('The new cases')
plt.title('The new cases of Covid-19 per day in Vietnam in 2020')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()