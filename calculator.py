distance = input('Pleace enter distance ran in kilometers:')
distance = float(distance)
time = input('Please enter total time of workout in the following format h.m:')
time = float(time)

pace = time/distance
print('Your pace was:', pace)