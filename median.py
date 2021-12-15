num = int(input('total numbers: '))
total_sum = 0
 
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
 
avg = total_sum/num
print('Average is :', avg)