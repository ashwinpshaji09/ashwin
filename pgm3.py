row = []
rowlength = int(input("enter the length of the row: "))
while True:
    if 5 <= rowlength <= 15:
        break        
    else:
        print("\nerror: Given row r, 5 ≤ r.length ≤ 15\nenter again\n")
        rowlength = int(input("enter the length of the row: "))
        

while rowlength > 0:
    x=int(input("enter the height(<200) or -1 if its a tree:"))
    if x >200:
        print("\nerror: maximum heigth is 200\nenter again\n")
        continue
    row.append(x)
    rowlength -=1
print(row)

sorted = []
between = []

for i in row:
    if i != -1:
        between.append(i)
between.sort()
iter = 0
for i in row:
    if i != -1:
        sorted.append(between[iter])
        iter += 1
    else:
        sorted.append(-1)
print(sorted)


'''
Test Case 1 :
input:= [-1, 150, 190, 170, -1, -1, 160, 180]
output:= [-1, 150, 160, 170, -1, -1, 180, 190]

Test Case 2 :
input:=[15, 78, 45, 32, 65, 59, 96]
output:=[15, 32, 45, 59, 65, 78, 96]

Test Case 3 :
input:=[8, 9, 6, 1, 2, 7]
output:=[1, 2, 6, 7, 8, 9]
'''
