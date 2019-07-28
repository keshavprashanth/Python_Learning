def checkPalindrome(inputString):
    reverse_string = inputString[::-1]
    if inputString == reverse_string:
        return True
    else:
        return False

print (checkPalindrome('ITATI'))