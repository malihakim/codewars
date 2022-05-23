def create_phone_number(n):
    areaCode = '(' + str(n[0]) + str(n[1]) + str(n[2]) + ') '
    nextThree = str(n[3]) + str(n[4]) + str(n[5]) + '-'
    lastFour = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    print(areaCode + nextThree + lastFour)

def create(n):
    print('({}{}{}) {}{}{}-{}{}{}{}'.format(*n))


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
create([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


    
