numbers = [10, 25, 8, 40, 15, 30]
key = int(input("Enter the number to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at index", i)
        found = True
        break
if not found:
    print("Element not found")