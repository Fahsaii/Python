def Check_Rate(sales):
    Rate = [0.30, 0.25, 0.15, 0.10, 0.05, 0.0]
    TotalSales = [1000000.0, 750000.0, 50000.0, 25000.0, 10000.0, 1.0, 0]
    for n in range(len(TotalSales)):
        if sales > TotalSales[n]:
            return(Rate[n])
Sales = []
count = 1
done = True
while done:
    sale = float(input(f'Enter sale {count} (-1 to Exit):'))
    if sale > -1.0:
        Sales += (sale,)
        count += 1
    elif sale == -1:
        break
Totals = sum(Sales)
print(f'Total sales : {Totals}')
Rate = Check_Rate(Totals)
print(f'Commission Rate : {Rate*100}%')
Commision = Totals * Rate 
print(f'Total Commision : {Commision}')