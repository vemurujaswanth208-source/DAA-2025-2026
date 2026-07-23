numbers = [5, 10, 15, 20, 25, 30, 35, 40]
key = int(input("Enter the number to search: "))
start = 0
end = len(numbers) - 1
while start <= end:
    mid = (start + end) // 2

    if key == numbers[mid]:
        print("Element found at index", mid)
        break

    elif key > numbers[mid]:
        start = mid + 1

    else:
        end = mid - 1
if start > end:
    print("Element not found")