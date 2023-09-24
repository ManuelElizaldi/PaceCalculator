def paceCalculator(time, distance, measurement):
    time = time.split(',')
    # Getting time values
    hours = float(time[0])
    minutes = float(time[1])
    seconds = float(time[2])
    
    # Formatting distance value
    distance = float(distance.replace(',', '.'))
    
    if hours > 0:
        # Converting seconds to decimals
        seconds = seconds/100

        # Convert hours to minutes
        hours = 2 
        hours2minutes = hours * 60
        minutes = hours2minutes + minutes

        # Calculating pace
        pace = minutes/float(distance)

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

def paceConverter(measurement, pace):
# Converting pace to the opposite measurement. i.e. km -> m or m -> km
    if measurement == 'km' or measurement == 'kilometer' or measurement == 'k':
        pace_conversion = pace * 1.6093491499172796
        print('Your pace in miles is:',round(pace_conversion,3), 'minutes per mile')

    elif measurement == 'mi' or measurement == 'miles' or measurement == 'm':
        pace_conversion = pace / 1.6093491499172796
        print('Your pace in kilometers is:',round(pace_conversion,3), 'minutes per kilometers')
        
    return pace_conversion