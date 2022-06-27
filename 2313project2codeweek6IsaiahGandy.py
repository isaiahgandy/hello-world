codedText = input("Enter the coded text: ")
distanceValue = int(input("Enter distance value: "))
result = ""
for ch in codedText:
    result += chr(ord(ch)-distanceValue)
print("" + result)
