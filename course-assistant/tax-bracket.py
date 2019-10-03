# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Lab 2: Tax Calculator                 |
# Nathan Stouffer                       |
# Date: September 10, 2019              |
# ---------------------------------------
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2018.  |
# ---------------------------------------

# My code is in the subsequent method

def unmarried_individual_tax(income):
    ## list to store lower bounds of a given bracket (descending order)
    lower_bounds = [ 510300, 204100, 160725, 84200, 39475, 9700, 0 ]
    ## list to store tax rates for a given brack (descending order)
    rates = [ 0.37, 0.35, 0.32, 0.24, 0.22, 0.12, 0.1 ]

    ## running total of tax owed
    tax_owed = 0
    for i in range(0, 7):
        if (income > lower_bounds[i]):
            ## taxable income in a given bracket
            taxable = income - lower_bounds[i]
            ## rate in current tax bracket
            rate = rates[i]
            ## add on to the total tax owed
            tax_owed += (taxable * rate)

            ## reset income to largest value in the next lowest tax bracket
            income = lower_bounds[i]

    return tax_owed

# ---------------------------------------

def process(income):
    print("The 2018 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():
    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7

# ---------------------------------------

main()
