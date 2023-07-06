def compound_interest(principal, rate_of_interest, number, time):
    amount = principal * pow((1 + (rate_of_interest/number)), number * time)
    ci = amount - principal
    return ci
def main_function():
    print("WELCOME TO XYZ BANK")
    Acnum=int(input("Please enter your account number :") )
    num=str(Acnum)
    if(len(num)==12):
        p = float(input("Enter the Loan Amount: "))
        r = float(0.05)
        n = float(12)
        t = float(input("Enter the due period: "))
        ci = compound_interest(p, r, n, t)
        print()
        print("Your intrest amount will be : %2f" %ci)
        print("THANK YOU")
    else:
            print("Enter a valid account number")

main_function()