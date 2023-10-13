import pandas as pd
import streamlit as st

def paceCalculator(time, distance, measurement):
    
    # Time variable is a string, we can split it into parts [2,44,0] with split, then handle each time part
    try:
        time = time.split(':')
        if len(time) != 3:
            hours = float(time[0])
            minutes = 0
            seconds = 0
        # Getting time values
        else:
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
    try:
        # Handling some string stuff
        pace = float(pace.replace(',', '.').replace(':','.'))
    
# Converting pace to the opposite measurement. i.e. km -> m or m -> km
        if measurement == 'Kilometers' or measurement == 'km' or measurement == 'kilometer' or measurement == 'k':
            # here we are converting to miles and then handling time format
            pace_conversion = (pace * 1.6093491499172796) - ((pace * 1.6093491499172796)%1) +  ((((pace * 1.6093491499172796)%1) * 60)/100)
            st.write('Your pace is:',round(pace_conversion,3), 'minutes per mile')

        elif measurement == 'Miles' or measurement == 'mi' or measurement == 'miles' or measurement == 'm':
            # in this formula first, we convert pace to time format then we do the conversion
            pace_conversion = (pace - pace%1 + (pace%1*100)/60)/1.6093491499172796
            st.write('Your pace is:',round(pace_conversion,3), 'minutes per kilometers')
        return pace_conversion
    
    except ValueError:
        st.write('Invalid pace format. Please enter 0.0.')
    except ZeroDivisionError:
        return 'Division by zero is not allowed'
    
def UnitConverter(measurement, distance):
    try:
        # Handling some string stuff
        distance = float(distance.replace(',', '.').replace(':', '.'))

        if measurement == 'Kilometers' or measurement == 'km' or measurement == 'kilometer' or measurement == 'k':
            result = distance * 0.621371
            st.write(f'Your distance in miles is:',round(result, 2))

        elif measurement == 'Miles' or measurement == 'mi' or measurement == 'miles' or measurement == 'm':
            result = distance * 1.6
            st.write(f'Your distance in kilometers is:', round(result, 2))
        
        return result

    except ValueError:
        st.write('Invalid distance format. Please enter 0.0.')


df = [
{
	"Minutes Per Kilometers": "7:30", 
	"Minutes Per Mile": "12:04", 
	"5k": "0:37:30", 
	"10k": "1:15:00", 
	"Half Marathon": "2:38:15", 
	"Marathon": "5:16:30"}, 
{
	"Minutes Per Kilometers": "7:25", 
	"Minutes Per Mile": "11:55", 
	"5k": "0:37:02", 
	"10k": "1:14:04", 
	"Half Marathon": "2:36:17", 
	"Marathon": "5:12:35"}, 
{
	"Minutes Per Kilometers": "7:19", 
	"Minutes Per Mile": "11:47", 
	"5k": "0:36:35", 
	"10k": "1:13:10", 
	"Half Marathon": "2:34:23", 
	"Marathon": "5:08:46"}, 
{
	"Minutes Per Kilometers": "7:14", 
	"Minutes Per Mile": "11:38", 
	"5k": "0:36:08", 
	"10k": "1:12:17", 
	"Half Marathon": "2:32:31", 
	"Marathon": "5:05:03"}, 
{
	"Minutes Per Kilometers": "7:08", 
	"Minutes Per Mile": "11:30", 
	"5k": "0:35:42", 
	"10k": "1:11:25", 
	"Half Marathon": "2:30:42", 
	"Marathon": "5:01:25"}, 
{
	"Minutes Per Kilometers": "7:04", 
	"Minutes Per Mile": "11:22", 
	"5k": "0:35:17", 
	"10k": "1:10:35", 
	"Half Marathon": "2:28:56", 
	"Marathon": "4:57:52"}, 
{
	"Minutes Per Kilometers": "6:59", 
	"Minutes Per Mile": "11:14", 
	"5k": "0:34:53", 
	"10k": "1:09:46", 
	"Half Marathon": "2:27:12", 
	"Marathon": "4:54:25"}, 
{
	"Minutes Per Kilometers": "6:54", 
	"Minutes Per Mile": "11:06", 
	"5k": "0:34:28", 
	"10k": "1:08:57", 
	"Half Marathon": "2:25:31", 
	"Marathon": "4:51:02"}, 
{
	"Minutes Per Kilometers": "6:49", 
	"Minutes Per Mile": "10:58", 
	"5k": "0:34:05", 
	"10k": "1:08:10", 
	"Half Marathon": "2:23:51", 
	"Marathon": "4:47:43"}, 
{
	"Minutes Per Kilometers": "6:44", 
	"Minutes Per Mile": "10:51", 
	"5k": "0:33:42", 
	"10k": "1:07:24", 
	"Half Marathon": "2:22:14", 
	"Marathon": "4:44:29"}, 
{
	"Minutes Per Kilometers": "6:40", 
	"Minutes Per Mile": "10:44", 
	"5k": "0:33:20", 
	"10k": "1:06:40", 
	"Half Marathon": "2:20:40", 
	"Marathon": "4:41:20"}, 
{
	"Minutes Per Kilometers": "6:35", 
	"Minutes Per Mile": "10:37", 
	"5k": "0:32:58", 
	"10k": "1:05:56", 
	"Half Marathon": "2:19:07", 
	"Marathon": "4:38:14"}, 
{
	"Minutes Per Kilometers": "6:31", 
	"Minutes Per Mile": "10:30", 
	"5k": "0:32:36", 
	"10k": "1:05:13", 
	"Half Marathon": "2:17:36", 
	"Marathon": "4:35:13"}, 
{
	"Minutes Per Kilometers": "6:27", 
	"Minutes Per Mile": "10:23", 
	"5k": "0:32:15", 
	"10k": "1:04:30", 
	"Half Marathon": "2:16:07", 
	"Marathon": "4:32:15"}, 
{
	"Minutes Per Kilometers": "6:23", 
	"Minutes Per Mile": "10:16", 
	"5k": "0:31:54", 
	"10k": "1:03:49", 
	"Half Marathon": "2:14:40", 
	"Marathon": "4:29:21"}, 
{
	"Minutes Per Kilometers": "6:19", 
	"Minutes Per Mile": "10:10", 
	"5k": "0:31:34", 
	"10k": "1:03:09", 
	"Half Marathon": "2:13:15", 
	"Marathon": "4:26:31"}, 
{
	"Minutes Per Kilometers": "6:15", 
	"Minutes Per Mile": "10:04", 
	"5k": "0:31:15", 
	"10k": "1:02:30", 
	"Half Marathon": "2:11:52", 
	"Marathon": "4:23:45"}, 
{
	"Minutes Per Kilometers": "6:11", 
	"Minutes Per Mile": "9:57", 
	"5k": "0:30:55", 
	"10k": "1:01:51", 
	"Half Marathon": "2:10:30", 
	"Marathon": "4:21:01"}, 
{
	"Minutes Per Kilometers": "6:07", 
	"Minutes Per Mile": "9:51", 
	"5k": "0:30:36", 
	"10k": "1:01:13", 
	"Half Marathon": "2:09:11", 
	"Marathon": "4:18:22"}, 
{
	"Minutes Per Kilometers": "6:04", 
	"Minutes Per Mile": "9:45", 
	"5k": "0:30:18", 
	"10k": "1:00:36", 
	"Half Marathon": "2:07:52", 
	"Marathon": "4:15:45"}, 
{
	"Minutes Per Kilometers": "6:00", 
	"Minutes Per Mile": "9:40", 
	"5k": "0:30:00", 
	"10k": "1:00:00", 
	"Half Marathon": "2:06:36", 
	"Marathon": "4:13:12"}, 
{
	"Minutes Per Kilometers": "5:56", 
	"Minutes Per Mile": "9:34", 
	"5k": "0:29:42", 
	"10k": "0:59:24", 
	"Half Marathon": "2:05:20", 
	"Marathon": "4:10:41"}, 
{
	"Minutes Per Kilometers": "5:53", 
	"Minutes Per Mile": "9:28", 
	"5k": "0:29:24", 
	"10k": "0:58:49", 
	"Half Marathon": "2:04:07", 
	"Marathon": "4:08:14"}, 
{
	"Minutes Per Kilometers": "5:50", 
	"Minutes Per Mile": "9:22", 
	"5k": "0:29:07", 
	"10k": "0:58:15", 
	"Half Marathon": "2:02:54", 
	"Marathon": "4:05:49"}, 
{
	"Minutes Per Kilometers": "5:46", 
	"Minutes Per Mile": "9:17", 
	"5k": "0:28:50", 
	"10k": "0:57:41", 
	"Half Marathon": "2:01:43", 
	"Marathon": "4:03:27"}, 
{
	"Minutes Per Kilometers": "5:43", 
	"Minutes Per Mile": "9:12", 
	"5k": "0:28:34", 
	"10k": "0:57:08", 
	"Half Marathon": "2:00:34", 
	"Marathon": "4:01:08"}, 
{
	"Minutes Per Kilometers": "5:40", 
	"Minutes Per Mile": "9:07", 
	"5k": "0:28:18", 
	"10k": "0:56:36", 
	"Half Marathon": "1:59:26", 
	"Marathon": "3:58:52"}, 
{
	"Minutes Per Kilometers": "5:37", 
	"Minutes Per Mile": "9:01", 
	"5k": "0:28:02", 
	"10k": "0:56:04", 
	"Half Marathon": "1:58:19", 
	"Marathon": "3:56:38"}, 
{
	"Minutes Per Kilometers": "5:34", 
	"Minutes Per Mile": "8:56", 
	"5k": "0:27:46", 
	"10k": "0:55:33", 
	"Half Marathon": "1:57:13", 
	"Marathon": "3:54:26"}, 
{
	"Minutes Per Kilometers": "5:30", 
	"Minutes Per Mile": "8:52", 
	"5k": "0:27:31", 
	"10k": "0:55:02", 
	"Half Marathon": "1:56:08", 
	"Marathon": "3:52:17"}, 
{
	"Minutes Per Kilometers": "5:27", 
	"Minutes Per Mile": "8:47", 
	"5k": "0:27:16", 
	"10k": "0:54:32", 
	"Half Marathon": "1:55:05", 
	"Marathon": "3:50:10"}, 
{
	"Minutes Per Kilometers": "5:25", 
	"Minutes Per Mile": "8:42", 
	"5k": "0:27:01", 
	"10k": "0:54:03", 
	"Half Marathon": "1:54:03", 
	"Marathon": "3:48:06"}, 
{
	"Minutes Per Kilometers": "5:22", 
	"Minutes Per Mile": "8:37", 
	"5k": "0:26:47", 
	"10k": "0:53:34", 
	"Half Marathon": "1:53:02", 
	"Marathon": "3:46:04"}, 
{
	"Minutes Per Kilometers": "5:19", 
	"Minutes Per Mile": "8:33", 
	"5k": "0:26:32", 
	"10k": "0:53:05", 
	"Half Marathon": "1:52:02", 
	"Marathon": "3:44:04"}, 
{
	"Minutes Per Kilometers": "5:16", 
	"Minutes Per Mile": "8:28", 
	"5k": "0:26:18", 
	"10k": "0:52:37", 
	"Half Marathon": "1:51:03", 
	"Marathon": "3:42:06"}, 
{
	"Minutes Per Kilometers": "5:13", 
	"Minutes Per Mile": "8:24", 
	"5k": "0:26:05", 
	"10k": "0:52:10", 
	"Half Marathon": "1:50:05", 
	"Marathon": "3:40:10"}, 
{
	"Minutes Per Kilometers": "5:10", 
	"Minutes Per Mile": "8:19", 
	"5k": "0:25:51", 
	"10k": "0:51:43", 
	"Half Marathon": "1:49:08", 
	"Marathon": "3:38:16"}, 
{
	"Minutes Per Kilometers": "5:08", 
	"Minutes Per Mile": "8:15", 
	"5k": "0:25:38", 
	"10k": "0:51:16", 
	"Half Marathon": "1:48:12", 
	"Marathon": "3:36:24"}, 
{
	"Minutes Per Kilometers": "5:05", 
	"Minutes Per Mile": "8:11", 
	"5k": "0:25:25", 
	"10k": "0:50:50", 
	"Half Marathon": "1:47:17", 
	"Marathon": "3:34:34"}, 
{
	"Minutes Per Kilometers": "5:02", 
	"Minutes Per Mile": "8:07", 
	"5k": "0:25:12", 
	"10k": "0:50:25", 
	"Half Marathon": "1:46:23", 
	"Marathon": "3:32:46"}, 
{
	"Minutes Per Kilometers": "5:00", 
	"Minutes Per Mile": "8:03", 
	"5k": "0:25:00", 
	"10k": "0:50:00", 
	"Half Marathon": "1:45:30", 
	"Marathon": "3:31:00"}, 
{
	"Minutes Per Kilometers": "4:58", 
	"Minutes Per Mile": "7:59", 
	"5k": "0:24:47", 
	"10k": "0:49:35", 
	"Half Marathon": "1:44:37", 
	"Marathon": "3:29:15"}, 
{
	"Minutes Per Kilometers": "4:55", 
	"Minutes Per Mile": "7:55", 
	"5k": "0:24:35", 
	"10k": "0:49:10", 
	"Half Marathon": "1:43:46", 
	"Marathon": "3:27:32"}, 
{
	"Minutes Per Kilometers": "4:53", 
	"Minutes Per Mile": "7:51", 
	"5k": "0:24:23", 
	"10k": "0:48:46", 
	"Half Marathon": "1:42:55", 
	"Marathon": "3:25:51"}, 
{
	"Minutes Per Kilometers": "4:50", 
	"Minutes Per Mile": "7:47", 
	"5k": "0:24:11", 
	"10k": "0:48:23", 
	"Half Marathon": "1:42:05", 
	"Marathon": "3:24:11"}, 
{
	"Minutes Per Kilometers": "4:48", 
	"Minutes Per Mile": "7:43", 
	"5k": "0:24:00", 
	"10k": "0:48:00", 
	"Half Marathon": "1:41:16", 
	"Marathon": "3:22:33"}, 
{
	"Minutes Per Kilometers": "4:46", 
	"Minutes Per Mile": "7:40", 
	"5k": "0:23:48", 
	"10k": "0:47:37", 
	"Half Marathon": "1:40:28", 
	"Marathon": "3:20:57"}, 
{
	"Minutes Per Kilometers": "4:43", 
	"Minutes Per Mile": "7:36", 
	"5k": "0:23:37", 
	"10k": "0:47:14", 
	"Half Marathon": "1:39:41", 
	"Marathon": "3:19:22"}, 
{
	"Minutes Per Kilometers": "4:41", 
	"Minutes Per Mile": "7:32", 
	"5k": "0:23:26", 
	"10k": "0:46:52", 
	"Half Marathon": "1:38:54", 
	"Marathon": "3:17:48"}, 
{
	"Minutes Per Kilometers": "4:39", 
	"Minutes Per Mile": "7:29", 
	"5k": "0:23:15", 
	"10k": "0:46:30", 
	"Half Marathon": "1:38:08", 
	"Marathon": "3:16:16"}, 
{
	"Minutes Per Kilometers": "4:37", 
	"Minutes Per Mile": "7:26", 
	"5k": "0:23:04", 
	"10k": "0:46:09", 
	"Half Marathon": "1:37:23", 
	"Marathon": "3:14:46"}, 
{
	"Minutes Per Kilometers": "4:35", 
	"Minutes Per Mile": "7:22", 
	"5k": "0:22:54", 
	"10k": "0:45:48", 
	"Half Marathon": "1:36:38", 
	"Marathon": "3:13:16"}, 
{
	"Minutes Per Kilometers": "4:33", 
	"Minutes Per Mile": "7:19", 
	"5k": "0:22:43", 
	"10k": "0:45:27", 
	"Half Marathon": "1:35:54", 
	"Marathon": "3:11:49"}, 
{
	"Minutes Per Kilometers": "4:31", 
	"Minutes Per Mile": "7:16", 
	"5k": "0:22:33", 
	"10k": "0:45:06", 
	"Half Marathon": "1:35:11", 
	"Marathon": "3:10:22"}, 
{
	"Minutes Per Kilometers": "4:29", 
	"Minutes Per Mile": "7:13", 
	"5k": "0:22:23", 
	"10k": "0:44:46", 
	"Half Marathon": "1:34:28", 
	"Marathon": "3:08:57"}, 
{
	"Minutes Per Kilometers": "4:26", 
	"Minutes Per Mile": "7:09", 
	"5k": "0:22:13", 
	"10k": "0:44:26", 
	"Half Marathon": "1:33:46", 
	"Marathon": "3:07:33"}, 
{
	"Minutes Per Kilometers": "4:25", 
	"Minutes Per Mile": "7:06", 
	"5k": "0:22:03", 
	"10k": "0:44:07", 
	"Half Marathon": "1:33:05", 
	"Marathon": "3:06:10"}, 
{
	"Minutes Per Kilometers": "4:23", 
	"Minutes Per Mile": "7:03", 
	"5k": "0:21:53", 
	"10k": "0:43:47", 
	"Half Marathon": "1:32:24", 
	"Marathon": "3:04:49"}, 
{
	"Minutes Per Kilometers": "4:21", 
	"Minutes Per Mile": "7:00", 
	"5k": "0:21:44", 
	"10k": "0:43:28", 
	"Half Marathon": "1:31:44", 
	"Marathon": "3:03:28"}, 
{
	"Minutes Per Kilometers": "4:19", 
	"Minutes Per Mile": "6:57", 
	"5k": "0:21:34", 
	"10k": "0:43:09", 
	"Half Marathon": "1:31:04", 
	"Marathon": "3:02:09"}, 
{
	"Minutes Per Kilometers": "4:17", 
	"Minutes Per Mile": "6:54", 
	"5k": "0:21:25", 
	"10k": "0:42:51", 
	"Half Marathon": "1:30:25", 
	"Marathon": "3:00:51"}, 
{
	"Minutes Per Kilometers": "4:16", 
	"Minutes Per Mile": "6:51", 
	"5k": "0:21:16", 
	"10k": "0:42:33", 
	"Half Marathon": "1:29:47", 
	"Marathon": "2:59:34"}, 
{
	"Minutes Per Kilometers": "4:14", 
	"Minutes Per Mile": "6:48", 
	"5k": "0:21:07", 
	"10k": "0:42:15", 
	"Half Marathon": "1:29:09", 
	"Marathon": "2:58:18"}, 
{
	"Minutes Per Kilometers": "4:12", 
	"Minutes Per Mile": "6:45", 
	"5k": "0:20:58", 
	"10k": "0:41:57", 
	"Half Marathon": "1:28:31", 
	"Marathon": "2:57:03"}, 
{
	"Minutes Per Kilometers": "4:10", 
	"Minutes Per Mile": "6:43", 
	"5k": "0:20:50", 
	"10k": "0:41:40", 
	"Half Marathon": "1:27:55", 
	"Marathon": "2:55:50"}, 
{
	"Minutes Per Kilometers": "4:08", 
	"Minutes Per Mile": "6:40", 
	"5k": "0:20:41", 
	"10k": "0:41:22", 
	"Half Marathon": "1:27:18", 
	"Marathon": "2:54:37"}, 
{
	"Minutes Per Kilometers": "4:07", 
	"Minutes Per Mile": "6:37", 
	"5k": "0:20:32", 
	"10k": "0:41:05", 
	"Half Marathon": "1:26:42", 
	"Marathon": "2:53:25"}, 
{
	"Minutes Per Kilometers": "4:05", 
	"Minutes Per Mile": "6:34", 
	"5k": "0:20:24", 
	"10k": "0:40:48", 
	"Half Marathon": "1:26:07", 
	"Marathon": "2:52:14"}, 
{
	"Minutes Per Kilometers": "4:03", 
	"Minutes Per Mile": "6:31", 
	"5k": "0:20:16", 
	"10k": "0:40:32", 
	"Half Marathon": "1:25:32", 
	"Marathon": "2:51:04"}, 
{
	"Minutes Per Kilometers": "4:02", 
	"Minutes Per Mile": "6:29", 
	"5k": "0:20:08", 
	"10k": "0:40:16", 
	"Half Marathon": "1:24:57", 
	"Marathon": "2:49:55"}, 
{
	"Minutes Per Kilometers": "4:00", 
	"Minutes Per Mile": "6:26", 
	"5k": "0:20:00", 
	"10k": "0:40:00", 
	"Half Marathon": "1:24:24", 
	"Marathon": "2:48:48"}, 
{
	"Minutes Per Kilometers": "3:58", 
	"Minutes Per Mile": "6:23", 
	"5k": "0:19:52", 
	"10k": "0:39:44", 
	"Half Marathon": "1:23:50", 
	"Marathon": "2:47:40"}, 
{
	"Minutes Per Kilometers": "3:57", 
	"Minutes Per Mile": "6:21", 
	"5k": "0:19:44", 
	"10k": "0:39:28", 
	"Half Marathon": "1:23:17", 
	"Marathon": "2:46:34"}, 
{
	"Minutes Per Kilometers": "3:55", 
	"Minutes Per Mile": "6:19", 
	"5k": "0:19:36", 
	"10k": "0:39:12", 
	"Half Marathon": "1:22:44", 
	"Marathon": "2:45:29"}, 
{
	"Minutes Per Kilometers": "3:54", 
	"Minutes Per Mile": "6:16", 
	"5k": "0:19:28", 
	"10k": "0:38:57", 
	"Half Marathon": "1:22:12", 
	"Marathon": "2:44:24"}, 
{
	"Minutes Per Kilometers": "3:52", 
	"Minutes Per Mile": "6:14", 
	"5k": "0:19:21", 
	"10k": "0:38:42", 
	"Half Marathon": "1:21:40", 
	"Marathon": "2:43:21"}, 
{
	"Minutes Per Kilometers": "3:51", 
	"Minutes Per Mile": "6:11", 
	"5k": "0:19:13", 
	"10k": "0:38:27", 
	"Half Marathon": "1:21:09", 
	"Marathon": "2:42:18"}, 
{
	"Minutes Per Kilometers": "3:49", 
	"Minutes Per Mile": "6:09", 
	"5k": "0:19:06", 
	"10k": "0:38:12", 
	"Half Marathon": "1:20:38", 
	"Marathon": "2:41:16"}, 
{
	"Minutes Per Kilometers": "3:48", 
	"Minutes Per Mile": "6:07", 
	"5k": "0:18:59", 
	"10k": "0:37:58", 
	"Half Marathon": "1:20:07", 
	"Marathon": "2:40:15"}, 
{
	"Minutes Per Kilometers": "3:46", 
	"Minutes Per Mile": "6:04", 
	"5k": "0:18:52", 
	"10k": "0:37:44", 
	"Half Marathon": "1:19:37", 
	"Marathon": "2:39:14"}, 
{
	"Minutes Per Kilometers": "3:45", 
	"Minutes Per Mile": "6:02", 
	"5k": "0:18:45", 
	"10k": "0:37:30", 
	"Half Marathon": "1:19:07", 
	"Marathon": "2:38:15"}, 
{
	"Minutes Per Kilometers": "3:44", 
	"Minutes Per Mile": "6:00", 
	"5k": "0:18:38", 
	"10k": "0:37:16", 
	"Half Marathon": "1:18:38", 
	"Marathon": "2:37:16"}, 
{
	"Minutes Per Kilometers": "3:42", 
	"Minutes Per Mile": "5:58", 
	"5k": "0:18:31", 
	"10k": "0:37:02", 
	"Half Marathon": "1:18:08", 
	"Marathon": "2:36:17"}, 
{
	"Minutes Per Kilometers": "3:41", 
	"Minutes Per Mile": "5:55", 
	"5k": "0:18:24", 
	"10k": "0:36:48", 
	"Half Marathon": "1:17:40", 
	"Marathon": "2:35:20"}, 
{
	"Minutes Per Kilometers": "3:40", 
	"Minutes Per Mile": "5:53", 
	"5k": "0:18:17", 
	"10k": "0:36:35", 
	"Half Marathon": "1:17:11", 
	"Marathon": "2:34:23"}, 
{
	"Minutes Per Kilometers": "3:38", 
	"Minutes Per Mile": "5:51", 
	"5k": "0:18:10", 
	"10k": "0:36:21", 
	"Half Marathon": "1:16:43", 
	"Marathon": "2:33:27"}, 
{
	"Minutes Per Kilometers": "3:37", 
	"Minutes Per Mile": "5:49", 
	"5k": "0:18:04", 
	"10k": "0:36:08", 
	"Half Marathon": "1:16:15", 
	"Marathon": "2:32:31"}, 
{
	"Minutes Per Kilometers": "3:35", 
	"Minutes Per Mile": "5:47", 
	"5k": "0:17:57", 
	"10k": "0:35:55", 
	"Half Marathon": "1:15:48", 
	"Marathon": "2:31:37"}, 
{
	"Minutes Per Kilometers": "3:34", 
	"Minutes Per Mile": "5:45", 
	"5k": "0:17:51", 
	"10k": "0:35:42", 
	"Half Marathon": "1:15:21", 
	"Marathon": "2:30:42"}, 
{
	"Minutes Per Kilometers": "3:33", 
	"Minutes Per Mile": "5:43", 
	"5k": "0:17:45", 
	"10k": "0:35:30", 
	"Half Marathon": "1:14:54", 
	"Marathon": "2:29:49"}, 
{
	"Minutes Per Kilometers": "3:32", 
	"Minutes Per Mile": "5:41", 
	"5k": "0:17:38", 
	"10k": "0:35:17", 
	"Half Marathon": "1:14:28", 
	"Marathon": "2:28:56"}, 
{
	"Minutes Per Kilometers": "3:31", 
	"Minutes Per Mile": "5:39", 
	"5k": "0:17:32", 
	"10k": "0:35:05", 
	"Half Marathon": "1:14:02", 
	"Marathon": "2:28:04"}, 
{
	"Minutes Per Kilometers": "3:29", 
	"Minutes Per Mile": "5:37", 
	"5k": "0:17:26", 
	"10k": "0:34:53", 
	"Half Marathon": "1:13:36", 
	"Marathon": "2:27:12"}, 
{
	"Minutes Per Kilometers": "3:28", 
	"Minutes Per Mile": "5:35", 
	"5k": "0:17:20", 
	"10k": "0:34:40", 
	"Half Marathon": "1:13:10", 
	"Marathon": "2:26:21"}, 
{
	"Minutes Per Kilometers": "3:27", 
	"Minutes Per Mile": "5:33", 
	"5k": "0:17:14", 
	"10k": "0:34:28", 
	"Half Marathon": "1:12:45", 
	"Marathon": "2:25:31"}, 
{
	"Minutes Per Kilometers": "3:26", 
	"Minutes Per Mile": "5:31", 
	"5k": "0:17:08", 
	"10k": "0:34:17", 
	"Half Marathon": "1:12:20", 
	"Marathon": "2:24:41"}, 
{
	"Minutes Per Kilometers": "3:25", 
	"Minutes Per Mile": "5:29", 
	"5k": "0:17:02", 
	"10k": "0:34:05", 
	"Half Marathon": "1:11:55", 
	"Marathon": "2:23:51"}, 
{
	"Minutes Per Kilometers": "3:23", 
	"Minutes Per Mile": "5:28", 
	"5k": "0:16:56", 
	"10k": "0:33:53", 
	"Half Marathon": "1:11:31", 
	"Marathon": "2:23:03"}, 
{
	"Minutes Per Kilometers": "3:22", 
	"Minutes Per Mile": "5:25", 
	"5k": "0:16:51", 
	"10k": "0:33:42", 
	"Half Marathon": "1:11:07", 
	"Marathon": "2:22:14"}, 
{
	"Minutes Per Kilometers": "3:21", 
	"Minutes Per Mile": "5:23", 
	"5k": "0:16:45", 
	"10k": "0:33:31", 
	"Half Marathon": "1:10:43", 
	"Marathon": "2:21:27"}, 
{
	"Minutes Per Kilometers": "3:20", 
	"Minutes Per Mile": "5:22", 
	"5k": "0:16:40", 
	"10k": "0:33:20", 
	"Half Marathon": "1:10:20", 
	"Marathon": "2:20:40"}, 
{
	"Minutes Per Kilometers": "3:19", 
	"Minutes Per Mile": "5:20", 
	"5k": "0:16:34", 
	"10k": "0:33:08", 
	"Half Marathon": "1:09:56", 
	"Marathon": "2:19:53"}, 
{
	"Minutes Per Kilometers": "3:18", 
	"Minutes Per Mile": "5:19", 
	"5k": "0:16:29", 
	"10k": "0:32:58", 
	"Half Marathon": "1:09:33", 
	"Marathon": "2:19:07"}, 
{
	"Minutes Per Kilometers": "3:17", 
	"Minutes Per Mile": "5:17", 
	"5k": "0:16:23", 
	"10k": "0:32:47", 
	"Half Marathon": "1:09:10", 
	"Marathon": "2:18:21"}, 
{
	"Minutes Per Kilometers": "3:16", 
	"Minutes Per Mile": "5:15", 
	"5k": "0:16:18", 
	"10k": "0:32:36", 
	"Half Marathon": "1:08:48", 
	"Marathon": "2:17:36"}, 
{
	"Minutes Per Kilometers": "3:14", 
	"Minutes Per Mile": "5:13", 
	"5k": "0:16:12", 
	"10k": "0:32:25", 
	"Half Marathon": "1:08:25", 
	"Marathon": "2:16:51"}, 
{
	"Minutes Per Kilometers": "3:14", 
	"Minutes Per Mile": "5:11", 
	"5k": "0:16:07", 
	"10k": "0:32:15", 
	"Half Marathon": "1:08:03", 
	"Marathon": "2:16:07"}, 
{
	"Minutes Per Kilometers": "3:13", 
	"Minutes Per Mile": "5:10", 
	"5k": "0:16:02", 
	"10k": "0:32:05", 
	"Half Marathon": "1:07:42", 
	"Marathon": "2:15:24"}, 
{
	"Minutes Per Kilometers": "3:11", 
	"Minutes Per Mile": "5:08", 
	"5k": "0:15:57", 
	"10k": "0:31:54", 
	"Half Marathon": "1:07:20", 
	"Marathon": "2:14:40"}, 
{
	"Minutes Per Kilometers": "3:10", 
	"Minutes Per Mile": "5:07", 
	"5k": "0:15:52", 
	"10k": "0:31:44", 
	"Half Marathon": "1:06:59", 
	"Marathon": "2:13:58"}, 
{
	"Minutes Per Kilometers": "3:10", 
	"Minutes Per Mile": "5:05", 
	"5k": "0:15:47", 
	"10k": "0:31:34", 
	"Half Marathon": "1:06:37", 
	"Marathon": "2:13:15"}, 
{
	"Minutes Per Kilometers": "3:08", 
	"Minutes Per Mile": "5:04", 
	"5k": "0:15:42", 
	"10k": "0:31:24", 
	"Half Marathon": "1:06:16", 
	"Marathon": "2:12:33"}, 
{
	"Minutes Per Kilometers": "3:08", 
	"Minutes Per Mile": "5:02", 
	"5k": "0:15:37", 
	"10k": "0:31:14", 
	"Half Marathon": "1:05:56", 
	"Marathon": "2:11:52"}, 
{
	"Minutes Per Kilometers": "3:07", 
	"Minutes Per Mile": "5:00", 
	"5k": "0:15:32", 
	"10k": "0:31:05", 
	"Half Marathon": "1:05:35", 
	"Marathon": "2:11:11"}, 
{
	"Minutes Per Kilometers": "3:05", 
	"Minutes Per Mile": "4:59", 
	"5k": "0:15:27", 
	"10k": "0:30:55", 
	"Half Marathon": "1:05:15", 
	"Marathon": "2:10:30"}, 
{
	"Minutes Per Kilometers": "3:05", 
	"Minutes Per Mile": "4:57", 
	"5k": "0:15:23", 
	"10k": "0:30:46", 
	"Half Marathon": "1:04:55", 
	"Marathon": "2:09:50"}, 
{
	"Minutes Per Kilometers": "3:04", 
	"Minutes Per Mile": "4:56", 
	"5k": "0:15:18", 
	"10k": "0:30:36", 
	"Half Marathon": "1:04:35", 
	"Marathon": "2:09:11"}, 
{
	"Minutes Per Kilometers": "3:03", 
	"Minutes Per Mile": "4:54", 
	"5k": "0:15:13", 
	"10k": "0:30:27", 
	"Half Marathon": "1:04:15", 
	"Marathon": "2:08:31"}, 
{
	"Minutes Per Kilometers": "3:02", 
	"Minutes Per Mile": "4:53", 
	"5k": "0:15:09", 
	"10k": "0:30:18", 
	"Half Marathon": "1:03:56", 
	"Marathon": "2:07:52"}, 
{
	"Minutes Per Kilometers": "3:01", 
	"Minutes Per Mile": "4:51", 
	"5k": "0:15:04", 
	"10k": "0:30:09", 
	"Half Marathon": "1:03:37", 
	"Marathon": "2:07:14"}, 
{
	"Minutes Per Kilometers": "3:00", 
	"Minutes Per Mile": "4:50", 
	"5k": "0:14:59", 
	"10k": "0:29:59", 
	"Half Marathon": "1:03:17", 
	"Marathon": "2:06:35"}, 
{
	"Minutes Per Kilometers": "2:59", 
	"Minutes Per Mile": "4:48", 
	"5k": "0:14:55", 
	"10k": "0:29:51", 
	"Half Marathon": "1:02:59", 
	"Marathon": "2:05:58"}, 
{
	"Minutes Per Kilometers": "2:58", 
	"Minutes Per Mile": "4:47", 
	"5k": "0:14:51", 
	"10k": "0:29:42", 
	"Half Marathon": "1:02:40", 
	"Marathon": "2:05:20"}, 
{
	"Minutes Per Kilometers": "2:58", 
	"Minutes Per Mile": "4:46", 
	"5k": "0:14:46", 
	"10k": "0:29:33", 
	"Half Marathon": "1:02:21", 
	"Marathon": "2:04:43"}, 
{
	"Minutes Per Kilometers": "2:56", 
	"Minutes Per Mile": "4:44", 
	"5k": "0:14:42", 
	"10k": "0:29:24", 
	"Half Marathon": "1:02:03", 
	"Marathon": "2:04:07"}, 
{
	"Minutes Per Kilometers": "2:56", 
	"Minutes Per Mile": "4:43", 
	"5k": "0:14:38", 
	"10k": "0:29:16", 
	"Half Marathon": "1:01:45", 
	"Marathon": "2:03:30"}, 
{
	"Minutes Per Kilometers": "2:55", 
	"Minutes Per Mile": "4:41", 
	"5k": "0:14:33", 
	"10k": "0:29:07", 
	"Half Marathon": "1:01:27", 
	"Marathon": "2:02:54"}, 
{
	"Minutes Per Kilometers": "2:54", 
	"Minutes Per Mile": "4:40", 
	"5k": "0:14:29", 
	"10k": "0:28:59", 
	"Half Marathon": "1:01:09", 
	"Marathon": "2:02:19"}, 
{
	"Minutes Per Kilometers": "2:53", 
	"Minutes Per Mile": "4:38", 
	"5k": "0:14:25", 
	"10k": "0:28:50", 
	"Half Marathon": "1:00:51", 
	"Marathon": "2:01:43"}, 
{
	"Minutes Per Kilometers": "2:52", 
	"Minutes Per Mile": "4:37", 
	"5k": "0:14:21", 
	"10k": "0:28:42", 
	"Half Marathon": "1:00:34", 
	"Marathon": "2:01:08"}, 
{
	"Minutes Per Kilometers": "2:52", 
	"Minutes Per Mile": "4:36", 
	"5k": "0:14:17", 
	"10k": "0:28:34", 
	"Half Marathon": "1:00:17", 
	"Marathon": "2:00:34"}, 
{}
]