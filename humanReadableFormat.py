def format_duration(a):
    time = {'year':0, 'day':0, 'hour':0, 'minute':0, 'second':0} 
    
    if a < 1:
        return 'now'
    
    if a in range(1, 60):
        time['second'] += a
    
    if a in range(60, 3600):
        time['minute'] += a//60
        time['second'] += a%60
    
    if a in range(3600, 86400):
        time['hour'] += a//3600
        b = a%3600
        if b > 59: 
            time['minute'] += b//60
            time['second'] += b%60
        else:
            time['minute'] += b  
            
    if a in range(86400, 31536000):
        time['day'] += a//86400
        b = a%86400
        if b > 365:
            time['hour'] += b//3600
            c = b%3600
            if c > 59:
                time['minute'] += c//60
                time['second'] += c%60
            else:
                time['minute'] += c
        else:
            time['hour'] += b
    
    if a >= 31536000:
        time['year'] += a//31536000
        b = a%31536000
        if b > 86400:
            time['day'] += b//86400
            c = b%86400
            if c > 365:
                time['hour'] += c//3600
                d = c%3600
                if d > 59:
                    time['minute'] += d//60
                    time['second'] += d%60
                else:
                    time['minute'] += d
            else:
                time['hour'] += c
        else:
            time['day'] += b 
    
    timeList = []
    for key, value in time.items():
        if value != 0:
            if value > 1:
                timeFormat = '{} {}s'.format(value, key)
                timeList.append(timeFormat)
            else:
                timeFormat = '{} {}'.format(value, key)
                timeList.append(timeFormat)

    t = ', '.join(timeList[:-1])
    if t != '':
        return(t + ' and ' + timeList[-1])
    else:
        return(timeList[-1])

#print(format_duration(int(input('Please enter your number. \n'))))

while True:
    print('\n' + 'Please enter your number.')
    value = input()

    try:
        value = int(value)
    except:
        print('Please use numeric digits.')
        continue

    print(format_duration(value))

    print('\n' + 'Would you like to try again? (yes/no)')
    if input() == 'no':
        break
    
    
    





