# Task 4: Loops & Iterations
# Demonstrates for loop, while loop, break, continue, and range usage

print("1. Printing numbers from 1 to 100 using for loop:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# ----------------------------------------

print("2. Countdown timer using while loop:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Countdown finished!\n")

# ----------------------------------------

print("3. Demonstrating break and continue:")
for num in range(1, 11):
    if num == 5:
        print("Skipping number 5")
        continue
    if num == 8:
        print("Breaking loop at 8")
        break
    print(num)
print()

# ----------------------------------------

print("4. Iterating over characters in a string:")
word = "Python"
for char in word:
    print(char)
print()

# ----------------------------------------

print("5. Multiplication table of a number:")
number = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print()

# ----------------------------------------

print("6. Using range with step value (even numbers from 2 to 20):")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# ----------------------------------------

print("7. Loop with condition (real-world example: checking attendance):")
attendance = [1, 1, 0, 1, 0, 1]  # 1 = Present, 0 = Absent
present_count = 0

for status in attendance:
    if status == 1:
        present_count += 1

print("Total present days:", present_count)
