number_month,year = [int(e) for e in input('Enter Month Year : ').split()]
days30 = [4,6,9,11]
days31 = [1,3,5,7,8,10,12]
year = year-543 
if number_month in days30:
    result = 30
elif number_month in days31:
    result = 31
elif number_month == 2 and ((year%4 == 0 and year%100 != 0) or (year%400 == 0)) :
    result = 29
elif number_month == 2 and (year%4) != 0:
    result = 28
else:
    result = 'What is that month ?'
print(f'This month  have : {str(result)} days')