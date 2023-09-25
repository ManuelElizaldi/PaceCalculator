def paceCalculator(time, distance, measurement):
    import streamlit as st
    
    # Time variable is a string, we can split it into parts [2,44,0] with split, then handle each time part
    try:
        time = time.split(',')
        if len(time) != 3:
            st.write('Invalid time format. Please enter hours, minutes, and seconds separated by commas.')
  
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
            
        st.write('Your running pace was:',pace,'minutes per ', measurement)
        return pace    
        
    except ValueError as e:
        return str(e)
    except ZeroDivisionError:
        return 'Division by zero is not allowed'        


def paceConverter(measurement, pace):
    import streamlit as st
    try:
        # Handling some string stuff
        pace = float(pace.replace(',', '.'))
        pace = float(pace)
    
# Converting pace to the opposite measurement. i.e. km -> m or m -> km
        if measurement == 'Kilometers' or measurement == 'km' or measurement == 'kilometer' or measurement == 'k':
            pace_conversion = pace * 1.6093491499172796
            st.write('Your pace in miles is:',round(pace_conversion,3), 'minutes per mile')

        elif measurement == 'Miles' or measurement == 'mi' or measurement == 'miles' or measurement == 'm':
            pace_conversion = pace / 1.6093491499172796
            st.write('Your pace in kilometers is:',round(pace_conversion,3), 'minutes per kilometers')
    
    except ValueError:
        st.write('Invalid pace format. Please enter 0.0.')
    except ZeroDivisionError:
        return 'Division by zero is not allowed'