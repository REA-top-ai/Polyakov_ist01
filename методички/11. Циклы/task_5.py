sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for i in sales_data:
    for j in i:
        scoops_sold += j

print(scoops_sold)