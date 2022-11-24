# Kiểm tra năm nhuận
a = int(input('Nhập năm: '))
if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print('Năm', a, 'là năm nhuận')
else:
    print('Năm', a, 'không phải là năm nhuận')