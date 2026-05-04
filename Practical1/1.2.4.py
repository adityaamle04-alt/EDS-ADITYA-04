# Input number of rows
n = int(input())

# Print number triangle pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
