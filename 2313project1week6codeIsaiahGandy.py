message = input("Enter a message: ")
distance = int(input("Enter distance value: "))
result = ""
for ch in message:
    result += chr(ord(ch)+distance)

print("\n"+result)
