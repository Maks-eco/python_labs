f_tr = open('text/tar_train.txt', 'w')
f_va = open('text/tar_valid.txt', 'w')
f_te = open('text/tar_test.txt', 'w')

num_str = 518#96368 #95413 #191779 
num_tr = (num_str // 10 * 6)
num_va = num_tr + (num_str // 10 * 2)
k = 0

# print(num_va, num_tr)

f = open('text/forestfires.csv', 'r')
line = f.readline()
while line:
    if k < num_va: #num_tr:
        f_tr.write(line)
    # if num_tr <= k < num_va:
    #     f_va.write(line)
    if k >= num_va:
        f_te.write(line)
    # print (line),
    k += 1
    line = f.readline()

print(num_va, num_tr, k)
f.close()
f_tr.close()
f_va.close()
f_te.close()
