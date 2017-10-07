import csv
import random

nlist = []

writer = csv.writer(open("file.csv", 'w'))
reader = csv.reader(nlist)
for x in range(1,400):
	x_rand = random.randint(1, 400)
	nlist.append(str(x_rand**2 - 50) + ", " + str(0.001 * x_rand) + ", " + str(x_rand))

for row in reader:
    writer.writerow(row)
