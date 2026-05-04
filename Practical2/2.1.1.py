# write the code..
# Initialize empty list
numbers = []

while True:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")
    
    print("Enter choice:", end=" ")
    choice = input()

    if choice == '1':
        print("Integer:", end=" ")
        try:
            num = int(input())
            numbers.append(num)
            print("List after adding:", numbers)
        except:
            print("Invalid input")

    elif choice == '2':
        if len(numbers) == 0:
            print("List is empty")
        else:
            print("Integer:", end=" ")
            try:
                num = int(input())
                if num in numbers:
                    numbers.remove(num)
                    print("List after removing:", numbers)
                else:
                    print("Element not found")
            except:
                print("Invalid input")

    elif choice == '3':
        if len(numbers) == 0:
            print("List is empty")
        else:
            print(numbers)

    elif choice == '4':
        break

    else:
        print("Invalid choice")