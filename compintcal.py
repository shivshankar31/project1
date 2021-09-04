# principle = principle amount

def compIntCal(*amount):
    principle = 0
    for each_amount in amount:
        principle = principle + each_amount
    print('Principle Amount is:', principle)
    # rate of interest input
    interest = float(input('Rate of intrest is:'))
    # time period input
    year = int(input('The time period (years): '))
    # Cal compound interest
    intamount = (principle*(pow((1 + interest/100), year))-principle)
    print('Total interest amount is:',intamount)
    total = principle + intamount
    print('#######################################')
    print('Account Balance:', total)
    print('#######################################')


compIntCal()
