def split(exp, finaldividends, finaldivisors):
    divisionindex = 0
    openBracketCount = 0
    closeBracketCount = 0

    for i in range(len(exp)):
        if exp[i] == "(":
            openBracketCount += 1
        elif exp[i] == ")":
            closeBracketCount += 1

        # If: Brackets on the left until correct division sign, e.g. (1/2)/(1/2)
        # Elif: No brackets on the left until correct division sign, e.g. 1/(1/2)
        if openBracketCount > 0 and (openBracketCount == closeBracketCount) and exp[i] == "/":
            divisionindex = i
        elif openBracketCount == 0 and closeBracketCount == 0 and exp[i] == "/":
            divisionindex = i

    # Extract dividend and divisor from expression
    dividend = exp[:divisionindex]
    divisor = exp[divisionindex + 1:]

    # Strip outer pairs of brackets
    while dividend[0] == "(" and dividend[-1] == ")":
        dividend = dividend[1:-1]

    while divisor[0] == "(" and divisor[-1] == ")":
        divisor = divisor[1:-1]
    
    # If there is a "/" sign in the dividend, run the function again
    # ,else add it to the dividend list because the path ends
    if "/" in dividend:
        split(dividend, finaldividends, finaldivisors)
    else:
        finaldividends.append(dividend)

    if "/" in divisor:
        # The order of finaldividends and finaldivisors is swapped
        # because dividing fraction by a fraction
        split(divisor, finaldivisors, finaldividends)
    else:
        finaldivisors.append(divisor)

expression = input()
finaldividends = []
finaldivisors = []
split(expression, finaldividends, finaldivisors)

numerator = 1
denominator = 1
for i in range(len(finaldividends)):
    numerator *= int(finaldividends[i])

for i in range(len(finaldivisors)):
    denominator *= int(finaldivisors[i])

print(numerator/denominator)

input("Press enter to exit.\n")