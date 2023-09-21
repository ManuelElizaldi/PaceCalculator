# ### Example run:
# - Distance 21.01 km
# - Pace 7:49/km
# - Time 2h 44m

try:
    # Asking user for this time
    time = input('Enter your time in the following format: hours, minutes, seconds')
    time = time.split(',')
    
    # From the input, getting the hours, minutes and seconds
    hours = float(time[0])
    minutes = float(time[1])
    seconds = float(time[2])
    
except:
    print('Please enter time in the correct format: h,m,s')

distance = float(input('What distance did you run? Format: 0.0'))
format = input('Are you measuring in kilometers or miles? Please enter: km or m')


# Converting seconds to decimals
seconds = seconds/100

# Convert hours to minutes
hours = 2 
hours2minutes = hours * 60
minutes = hours2minutes + minutes


# Calculating pace
pace = minutes/distance
conversion_pace = pace

# Converting pace decimals into actual minutes
pace_decimals = pace % 1
pace_decimals = (pace_decimals * 60)/100

pace = round(pace - (pace%1) + pace_decimals,2)


# Printing pace
print(f'Your was: {pace}/{format}')


# Converting pace to the opposite format. i.e. km -> m or m -> km
conversion_pace