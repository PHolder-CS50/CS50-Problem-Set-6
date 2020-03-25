# Check input strings to verify they're valid credit card (CC) numbers
# using Luhn’s algorithm and then if valid, it identifies what type
# of CC it is from Amex, Visa and MasterCard


from cs50 import get_int


# prompt for potential CC number, and if it is valid output
# the CC type, or else say INVALID
def main():
    potentialCCNumber = getPotentialCCNumber()
    if potentialCCNumber < 0:
        print("INVALID")
    elif not isValidCC(potentialCCNumber):
        print("INVALID")
    else:
        print(indentifyCardType(potentialCCNumber))


# Get a potential CC number as input from the user
def getPotentialCCNumber():
    num = get_int("Number: ")
    if num >= 1000000000000 and num <= 9999999999999999:
        return num
    else:
        return -1


# Implement Luhn’s algorithm to check a potential CC to see
# if the checksum is correct and return True or False accordingly
def isValidCC(potentialCCNumber):
    result = True
    n = potentialCCNumber
    sum = 0
    dn = 1
    while n > 0:
        # print(f"n={n}")
        digit = n % 10
        n = int(n / 10)
        if dn % 2 == 0:
            digit *= 2
            if digit > 9:
                sum += 1 + digit % 10
            else:
                sum += digit
        else:
            sum += digit
        dn += 1
    # print(f"sum={sum}")
    if sum % 10 == 0:
        return True
    return False


# Returns the number of digits in the CC number as well as the first
# two digits
def getFirstTwoDigits(CCNumber):
    n = CCNumber
    digit = 0
    numDigits = 0
    while n > 0:
        numDigits += 1
        last = digit
        digit = n % 10
        n = int(n / 10)
    return (numDigits, digit, last)


# Uses the length of the CC number as well as the first two digits
# to determine the card type and return it as a string
def indentifyCardType(CCNumber):
    numDigits, dig1, dig2 = getFirstTwoDigits(CCNumber)
    # print(f"numDigits={numDigits} dig1={dig1} dig2={dig2}")

    # AMEX has 15 digits, starting with 34 or 37
    if numDigits == 15 and dig1 == 3:
        if dig2 == 4 or dig2 == 7:
            return "AMEX"

    # VISA has 13 or 16 digits, starting with 4
    if numDigits == 13 or numDigits == 16:
        if dig1 == 4:
            return "VISA"

    # MC 16 digits, starting with 51, 52, 53, 54 or 55
    if numDigits == 16 and dig1 == 5:
        if dig2 > 0 and dig2 < 6:
            return "MASTERCARD"

    # Didn't recognize the type of card
    return "INVALID"


# Start the program
main()
