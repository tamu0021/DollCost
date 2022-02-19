up_unit = 150.
down_unit = 50.
bill_unit = 100.
bill_unit_now = 100

trials = 364

bill = bill_unit
percent = 1
for i in range(1, trials):
    if i % 2 == 1:
        bill = bill * (down_unit/bill_unit_now) + bill_unit / (down_unit / bill_unit)
        bill_unit_now = down_unit
        percent = percent * down_unit
    else:
        bill = bill * (up_unit/bill_unit_now) + bill_unit / (up_unit / bill_unit)
        bill_unit_now = up_unit
        percent = percent * up_unit
    
print(bill / (bill_unit_now * trials))
print(bill)
