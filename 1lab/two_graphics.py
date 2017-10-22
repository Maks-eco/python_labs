import csv
import matplotlib.pyplot as plt
import numpy as np
import copy

x1_list = []
x2_list = []
y_list = []

reader = csv.reader(open("file.csv", 'r'))

for row in reader:
    x1_list.append(float(row[0]))
    x2_list.append(float(row[1]))
    y_list.append(float(row[2]))
# 	print(row)

def prMaxMinAver( name, arr ):
    print(name + ": Max(" +  str(max(arr)) + ") Min(" + str(min(arr)) + ") Aver(" + str(np.mean(arr)) + ")")
    return np.mean(arr)

aver_x1 = prMaxMinAver( "x1", x1_list )
aver_x2 = prMaxMinAver( "x2", x2_list )
prMaxMinAver( "y", y_list )

fig = plt.figure()
ax1 = fig.add_subplot(121)
# A twin axis for list 4. This shares the x axis, but has a separate y axis
ax2 = fig.add_subplot(122)
# plt.plot(x1_list)
# plt.plot(x2_list)
# plt.ylabel('some numbers')
ax1.plot(x1_list, y_list, 'ro')
ax1.plot(x2_list, y_list, 'yo')
ax2.plot(y_list, x1_list, 'co')
ax2.plot(y_list, x2_list, 'bo')
plt.show()

writer = csv.writer(open("file_if.csv", 'w'))
reader = csv.reader(open("file.csv", 'r'))

for row in reader: 
    # print(row)   
    if float(row[0]) < aver_x1 or float(row[1]) < aver_x2:
        writer.writerow(row)
    	