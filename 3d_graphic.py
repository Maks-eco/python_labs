import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1_list = []
x2_list = []
y_list = []

reader = csv.reader(open("file.csv", 'r'))

for row in reader:
	x1_list.append(float(row[0]))
	x2_list.append(float(row[1]))
	y_list.append(float(row[2]))
	# print(row)
# print(x1_list, x2_list, y_list)
ax.scatter(x1_list, x2_list, y_list, color='b')
plt.show()

