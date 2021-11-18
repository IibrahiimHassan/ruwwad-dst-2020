word=input("enter a word:")
if (word[0]==word[-1] and word[1]==word[-2] or word[0]==word[-1]):
    print("it is a palindrome")
else:
    print(" it is not a palindrome")