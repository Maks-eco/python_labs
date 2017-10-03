import csv
# import matplotlib.pyplot as plt

# mylist = ['1 , 3 , s4', '2', '3', '4']
nlist = []

writer = csv.writer(open("/home/makskrug/py_prj/file.csv", 'w'))
reader = csv.reader(nlist)
for x in range(1,400):
	nlist.append(str(x**2 - 50) + ", " + str(0.001 * x) + ", " + str(x))
	# x1 = x^2 - 50
	# x2 = 0.001 * x
	# nlist.append(str(x1) + ", " + str(x2) + ", " + str(x))

# print(nlist)

for row in reader:
    writer.writerow(row)
