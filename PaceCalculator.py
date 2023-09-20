# Getting input to know if its miles or kms 
#measurement = input('What are you measuring?')

# First we start by getting the time and coverting to mintues - remember, pace is measured in mins
time = input('Please enter total time in the following format h.m:')
time = float(time)

# We need to be able to handle hours and minutes
if time >= 1.0:
    # Handling minutes
    minutes = time - 1
    total_minutes = round(minutes * 100)

    # Handling hours
    hours = time - minutes
    hours = hours * 60
    
    # Total time in minutes
    total_time_minutes = hours + total_minutes
else:
    total_time_minutes = time * 100

print(total_time_minutes)

# Getting distance
format = input('miles or kilometers?')
distance = input('Pleace enter distance ran in format 0.0 miles or kilometers:')
distance = float(distance)
print(distance)

# Calculating pace
pace = round(total_time_minutes/distance,2)
print('Your pace was:', pace, f'm/{format}')