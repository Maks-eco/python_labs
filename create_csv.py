import csv

nlist = []

writer = csv.writer(open("file.csv", 'w'))
reader = csv.reader(nlist)
for x in range(1,400):
	nlist.append(str(x**2 - 50) + ", " + str(0.001 * x) + ", " + str(x))

for row in reader:
    writer.writerow(row)
