# Credit Calculator v1.0

import math
import argparse

parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument('--type', type=str, help='Type of Credit')
parser.add_argument('--principal', type=int, help='Credit Principal')
parser.add_argument('--periods', type=int, help='Number of months')
parser.add_argument('--interest', type=float, help='Credit Interest')
parser.add_argument('--payment', type=int, help='Payment to be made')
args = parser.parse_args()

def differential_credit(principal, periods, interest):
    total = 0
    a1 = principal / periods
    i = interest / 1200
    for m in range(1, periods + 1):
        a2 = principal * (m - 1) / periods
        diff = a1 + i * (principal - a2)
        total += math.ceil(diff)
        print(f"Month {m}: paid out {math.ceil(diff)}")

    overpayment = total - principal
    print(f"Overpayment = {math.ceil(overpayment)}")


def annuity_credit(principal, periods, interest):
    i = interest / 1200
    den = ((1 + i) ** periods) - 1
    mul = i * ((1 + i) ** periods) / den
    annuity = math.ceil(principal * mul)
    overpayment = (annuity * periods) - principal

    print(f"Your annuity payment = {math.ceil(annuity)}!")
    print(f"Overpayment = {math.ceil(overpayment)}")

def annuity_principal(payment, periods, interest):
    i = interest / 1200
    den1 = i * ((1 + i) ** periods)
    den2 = ((1 + i) ** periods) - 1
    den = den1 / den2
    principal = payment / den

    print(f"Your credit principal = {math.floor(principal)}")
    overpayment = (payment * periods) - principal
    print(f"Overpayment = {math.ceil(overpayment)}!")


def annuity_periods(principal, payment, interest):
    i = interest / 1200
    den = payment - i * principal
    a = payment / den
    i += 1

    months = math.log(a, i)
    periods = math.ceil(months)

    if months == 1:
        print(f"It takes {math.ceil(months)} month to repay the credit!")
    else:
        years = math.floor(months / 12)
        months = math.ceil(months % 12)
        if months == 0:
            print(f"It takes {years} years to repay the credit!")
        elif months == 12:
            years += 1
            print(f"It takes {years} years to repay the credit!")
        else:
            print(f"It takes {years} years and {months} months to repay the credit!")

    overpayment = (payment * periods) - principal
    print(f"Overpayment = {math.ceil(overpayment)}")


if __name__ == "__main__":
    if args.type is None:
        print("Incorrect parameters")
    elif args.type == "diff":
        if args.principal is None or args.periods is None or args.interest is None or args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect parameters")
        else:
            differential_credit(args.principal, args.periods, args.interest)
    elif args.type == "annuity":
        if args.payment is None:
            if args.principal is None or args.periods is None or args.interest is None or args.principal < 0 or args.periods < 0 or args.interest < 0:
                print("Incorrect parameters")
            else:
                annuity_credit(args.principal, args.periods, args.interest)
        elif args.principal is None:
            if args.payment is None or args.periods is None or args.interest is None or args.payment < 0 or args.periods < 0 or args.interest < 0:
                print("Incorrect parameters")
            else:
                annuity_principal(args.payment, args.periods, args.interest)
        elif args.periods is None:
            if args.principal is None or args.payment is None or args.interest is None or args.principal < 0 or args.payment < 0 or args.interest < 0:
                print("Incorrect parameters")
            else:
                annuity_periods(args.principal, args.payment, args.interest)
