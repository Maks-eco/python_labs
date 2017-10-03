import csv
import matplotlib.pyplot as plt
import numpy as np
import copy

# mylist = ['1 , 3 , s4', '2', '3', '4']
x1_list = []
x2_list = []
y_list = []

# writer = csv.writer()
reader = csv.reader(open("/home/makskrug/py_prj/file.csv", 'r'))

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

# print(aver_x2, aver_x1)

# plt.plot(x1_list)
# plt.plot(x2_list)
# plt.ylabel('some numbers')
# plt.show()
writer = csv.writer(open("/home/makskrug/py_prj/file_if.csv", 'w'))
reader = csv.reader(open("/home/makskrug/py_prj/file.csv", 'r'))

for row in reader: 
    # print(row)   
    if float(row[0]) < aver_x1 or float(row[1]) < aver_x2:
        writer.writerow(row)
    	