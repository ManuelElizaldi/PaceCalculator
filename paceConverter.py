# ### Example run ###
# - Distance 21.01 km
# - Pace 7:49/km
# - Time 2h 44m
# 
# ### Another example:
# - Distance 6.44 km
# - Pace 7:20/km
# - Time 47m 16s
# 
# This is something similar to the end product:
# https://www.xconvert.com/unit-converter/minutes-per-kilometre-to-minutes-per-mile

try:
    # Asking user for this time
    time = input('Enter your time in the following format: hours, minutes, seconds:')
    time = time.split(',')
    
    # From the input, getting the hours, minutes and seconds
    hours = float(time[0])
    minutes = float(time[1])
    seconds = float(time[2])
    
except:
    print('Please enter time in the correct format: h,m,s:')

distance = float(input('What distance did you run? Format: 0.0:'))
measurement = input('Are you measuring in kilometers or miles? Please enter: km or m:')

def paceCalculator(time, distance, measurement):
    hours = float(time[0])
    minutes = float(time[1])
    seconds = float(time[2])
    
    if hours > 0:
        # Converting seconds to decimals
        seconds = seconds/100

        # Convert hours to minutes
        hours = 2 
        hours2minutes = hours * 60
        minutes = hours2minutes + minutes

        # Calculating pace
        pace = minutes/distance

        # Converting pace decimals into actual minutes
        pace_decimals = pace % 1
        pace_decimals = (pace_decimals * 60)/100

        pace = round(pace - (pace%1) + pace_decimals,2)
    
# Need to create code to handle when 0,x,x
    else:
        # Converting seconds to decimals
        seconds = seconds/100
        minutes = minutes + seconds
        
        # Calculating pace
        pace = minutes/distance

        # Converting pace decimals into actual minutes 
        pace_decimals = pace % 1
        pace_decimals = (pace_decimals * 60)/100

        pace = round(pace - (pace%1) + pace_decimals)
        
        # Printing pace
    print(f'Your was: {pace}/{measurement}')
    return pace
    


pace = paceCalculator(time,distance,measurement)

print(pace)

def paceConverter(measurement, pace):
# Converting pace to the opposite measurement. i.e. km -> m or m -> km
    if measurement == 'km' or measurement == 'kilometer' or measurement == 'k':
        pace_in_miles = pace * 1.6093491499172796
        print('Your pace in miles is:',round(pace_in_miles,3), 'minutes per mile')

    elif measurement == 'mi' or measurement == 'miles' or measurement == 'm':
        pace_in_kilometers = pace / 1.6093491499172796
        print('Your pace in kilometers is:',round(pace_in_kilometers,3), 'minutes per kilometers')

# Converting pace to the opposite measurement. i.e. km -> m or m -> km
if measurement == 'km' or measurement == 'kilometer' or measurement == 'k':
    pace_in_miles = pace * 1.6093491499172796
    print('Your pace in miles is:',round(pace_in_miles,3), 'minutes per mile')

elif measurement == 'mi' or measurement == 'miles' or measurement == 'm':
    pace_in_kilometers = pace / 1.6093491499172796
    print('Your pace in kilometers is:',round(pace_in_kilometers,3), 'minutes per kilometers')

if hours > 0:
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
    
# Need to create code to handle when 0,x,x
else:
    # Converting seconds to decimals
    seconds = seconds/100
    minutes = minutes + seconds
    
    # Calculating pace
    pace = minutes/distance
    conversion_pace = pace

    # Converting pace decimals into actual minutes 
    pace_decimals = pace % 1
    pace_decimals = (pace_decimals * 60)/100

    pace = round(pace - (pace%1) + pace_decimals)

# Printing pace
print(f'Your was: {pace}/{format}')

conversion_pace

# Converting pace to the opposite format. i.e. km -> m or m -> km
if format == 'km' or 'kilometer' or 'k':
    pace_in_miles = pace * 1.6093491499172796
    print('Your pace in miles is:',round(pace_in_miles,3))

elif format == 'mi' or 'miles' or 'm':
    pace_in_kilometers = pace / 1.6093491499172796
    print('Your pace in kilometers is:',round(pace_in_kilometers,3))





