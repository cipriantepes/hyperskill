import math
import sys
import argparse

# todo Refactor!!!!!


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', help='Choose annuity or diff')
    parser.add_argument('--payment', type=int, help='Monthly payment, not to use with diff')
    parser.add_argument('--principal', type=int)
    parser.add_argument('--periods', type=int, help='Number of months and/or years needed to repay')
    parser.add_argument('--interest', type=float)
    args = parser.parse_args()
    # print(sys.argv[1:])

    if len(sys.argv[1:]) < 4:
        print('Incorrect parameters')
        return False

    # if is not annuity or diff, don't continue
    if args.type not in ['annuity', 'diff']:
        print('Incorrect parameters')
        return False

    if args.type == 'diff' and args.payment:
        print('Incorrect parameters')
        return False

    if args.type == 'annuity' and not args.interest:
        print('Incorrect parameters')
        return False

    """for i in [args.payment, args.principal, args.periods]:
        if i < 1:
            print('Incorrect parameters')
            return False"""

    if not args.periods:
        return print_count_of_months(args.principal, args.payment, args.interest)

    if args.type == 'diff':
        return print_differentiated_payment(args.principal, args.periods, args.interest)

    if args.type == 'annuity' and args.payment:
        return print_credit_principal(args.payment, args.periods, args.interest)

    if args.type == 'annuity' and args.principal:
        return print_annuity_monthly(args.principal, args.periods, args.interest)

    pass


def print_count_of_months(user_principal, monthly_payment, interest_rate):
    interest_rate = calc_credit_interest(interest_rate)

    n = math.log(monthly_payment / (monthly_payment - interest_rate * user_principal), (1 + interest_rate))
    annuity_payment = math.ceil(user_principal * calc_credit_principal(interest_rate, math.ceil(n)))
    difference = n - int(n)
    years = n // 12
    months = math.ceil(n % 12)
    if months == 12:
        years += 1
        months = 0
    period = f'{str(round(years))} years'
    if months:
        period += f' and {str(months)} '
        period += 'month' if months == 1 else 'months'
    # print(n, difference, years, months)
    print(f'You need {period} to repay this credit!')
    print(f'Overpayment = {monthly_payment * math.ceil(n) - user_principal}')


def print_annuity_monthly(user_principal, user_months, interest_rate):
    interest_rate = calc_credit_interest(interest_rate)
    annuity_payment = math.ceil(user_principal * calc_credit_principal(interest_rate, user_months))
    print(f'Your annuity payment = {annuity_payment}!')
    # todo Calculate and print Overpayment
    print(f'Overpayment = {annuity_payment * user_months - user_principal}')


def print_credit_principal(monthly, user_months, interest_rate):
    interest_rate = calc_credit_interest(interest_rate)
    credit_principal = monthly / calc_credit_principal(interest_rate, user_months)
    print(f'Your credit principal = {int(credit_principal)}!')
    # todo Calculate and print Overpayment
    print(f'Overpayment = {monthly * user_months - int(credit_principal)}')

    return credit_principal


def print_differentiated_payment(principal, user_months, interest_rate):
    interest_rate = calc_credit_interest(interest_rate)
    overpayment = 0
    for i in range(user_months):
        paid = principal / user_months + interest_rate * (principal - (principal * (i + 1 - 1)) / user_months)
        overpayment += math.ceil(paid)
        print(f'Month {i + 1}: paid out {math.ceil(paid)}')
    print()
    print(f'Overpayment = {overpayment - principal}')


def calc_months_number(user_principal, monthly_payment, interest_rate):
    interest_rate = calc_credit_interest(interest_rate)

    n = math.log(monthly_payment / (monthly_payment - interest_rate * user_principal), (1 + interest_rate))
    return n - int(n)


def calc_credit_interest(interest):
    return float(interest) * 0.01 / 12


def calc_credit_principal(interest_rate, months):
    # todo check None for months
    interest_pow = math.pow(1 + interest_rate, months)
    return interest_rate * interest_pow / (interest_pow - 1)


def print_calc_options(options):
    print('What do you want to calculate?')
    print(','.join([f'\ntype "{opt}" - for {options[opt]["name"]}' for opt in options]).strip())

    return options[input()]['fn']()


def user_option(option):
    return methods[option]['fn']()


params = ['type', 'payment', 'principal', 'periods', 'interest']
types = ['annuity', 'diff']

methods = {
    'n': {
        'name': 'count of months',
        'fn': print_count_of_months
    },
    'a': {
        'name': 'annuity monthly payment',
        'fn': print_annuity_monthly
    },
    'p': {
        'name': 'credit principal',
        'fn': print_credit_principal
    }
}

handle_args()
# todo this was called on step 3/4
# print_calc_options(methods)
