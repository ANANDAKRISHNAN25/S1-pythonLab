#Adding 'ing' and 'ly'
string = input("Enter a string: ")
if string.endswith("ing"):
    print(string+"ly")
else:
    print(string+"ing","is the newly formed word")