def pallindrome(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]

    if rev == str:
        print("pallindrome")
    else:
        print("not pallindrome")

pallindrome("NAMAN")
pallindrome("CURSOR")