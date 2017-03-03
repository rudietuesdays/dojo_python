def change(cents):
    coins = {}
    dollar = 100
    half_dollar = 50
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    dollars = 0
    half_dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    if cents > 99:
        dollars = cents/dollar
        cents = cents%dollar
        print dollars, cents
    if cents > 24:
        quarters = cents/quarter
        cents = cents%quarter
        print quarters, cents
    if cents > 9:
        dimes = cents/dime
        cents =  cents%dime
        print dimes, cents
    if cents > 4:
        nickels = cents/nickel
        cents = cents%nickel
        print nickels, cents
    if cents > 1:
        pennies = cents/penny
        cents = cents%penny
        print pennies, cents

    coins = {
        'dollars': dollars,
        'quarters': quarters,
        'dimes': dimes,
        'nickels': nickels,
        'pennies': pennies,
    }
    print coins
    return coins

change(12)
