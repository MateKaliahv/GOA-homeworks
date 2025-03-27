# 1) Place your name in a variable and print all the vowels from the string.
name = "Your Name Here" # Replace with your actual name
vowels = "aeiouAEIOU"
vowel_chars = [char for char in name if char in vowels]
print("Vowels in the name:", vowel_chars)

# 2) True or False? Strings are mutable, Lists are immutable.
# Answer: False.

# 3) Explanation of the answer to the second task:
# Strings in Python are immutable, i.e., you cannot change them after they're formed.
# Lists are mutable, i.e., you can alter their contents (add, remove, or change elements).

### 4) Make an empty list and gather information about yourself.
user_info = []
for i in range(8):
user_info= input(f"Enter information about yourself (e.g., name, surname, age, etc.): ")
user_info.append(info)

print("User information:", user_info)

# 5) Class assignments:

# Ask the user for 10 values to put in a list and find out if they are even or odd.
numbers = []
for i in range(10):
num = int(input(f"Enter number {i + 1}: "))
numbers.append(num)

for number in numbers:
if number % 2 == 0:
print(f"{number} is even.")
else:
print(f"{number} is odd.")

# Ask the user for 5 names and determine the length.
names = []
for i in range(5):
name = input(f"Enter name {i + 1}: ")
names.append(name)

for name in names:
if len(name) > 5:
print("The name has more than five letters.")

# List of healthy food items.
healthy_foods = ["Fruits", "Vegetables", "Nuts", "Whole grains", "Fish"]

# Remove the first and last items from the list.
del healthy_foods[0] # Remove first item
del healthy_foods[-1] # Remove last item

print("Updated list of healthy foods:", healthy_foods)

# Create a list with at least 5 items where 1 item is different.
numbers_with_unique = [1, 2, 3, 4, 99, 5] # 99 is the unique element in the middle (not at the beginning or end)

# Get the unique element.
sorted_numbers = sorted(numbers_with_unique)

unique_element = None
for i in sorted_numbers:
if sorted_numbers.count(i) == 1:
unique_element = i
break

print("The unique element is:", unique_element)