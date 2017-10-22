import csv
import random
import pandas

# nlist = []

# writer = csv.writer(open("file.csv", 'w'))
# reader = csv.reader(nlist)
# for x in range(1,400):
# 	x_rand = random.randint(1, 400)
# 	nlist.append(str(x_rand**2 - 50) + ", " + str(0.001 * x_rand) + ", " + str(x_rand))
# Сгенерировать csv файл 
with open("file.csv", "w", newline="") as file: 
    data = csv.writer(file) 
    data.writerows([[(x**2 - 50), (0.001 * x), random.randint (0,100)] for x in range(0,400)]) 
file = pandas.read_csv("file.csv") 
file.head()