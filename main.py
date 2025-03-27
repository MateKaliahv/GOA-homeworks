# 1) What is the purpose of lists in Python:
# Python lists are a dynamic data structure that allows you to store an ordered list of items.
# Lists can contain mixed data types, including integers, strings, and even lists.
# They are mutable, and you can modify them by adding, removing, or modifying elements after they are created.
# Declaration syntax for a list is surrounding comma-separated values with square brackets [].
# Syntax: my_list = [1, 2, 3, "apple", "banana"].
# Python indexing for lists starts with 0; i.e., the first item is accessed with index 0, the second with index 1, etc.
# e.g., my_list[0] would print 1, and my_list[3] would print "apple".

# 2) Print a list of healthy foods.
healthy_foods = ["Fruits", "Vegetables", "Nuts", "Whole grains", "Fish"]
print("List of healthy foods:", healthy_foods)

# 3) Print the third favorite car model from the list of favorite car models.
favorite_cars = ["Tesla Model S", "Ferrari LaFerrari", "Porsche 911", "Lamborghini Aventador", "Ford Mustang"]
print("Third favorite car model:", favorite_cars[2]) # Index 2 is the third element

# 4) Create a list of numbers with 10+ elements and print the last element with negative indexing.
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print("Last element using negative indexing:", numbers[-1]) # -1 for the last element

# 5) Create a list of movie titles and print the second and fourth element without slicing.
movie_titles = ["Inception", "The Matrix", "Interstellar", "Avengers", "Titanic"]
print("Second movie title:", movie_titles[1]) # The second element is at index 1
print("Fourth movie title:", movie_titles[3]) # The fourth element is at index 3

# 6) Program to determine whether a number is prime.
def is_prime(num):
if num <= 1:
return False # 0 and 1 aren't prime numbers
for i in range(2, int(num ** 0.5) + 1): # Check factors between 2 and the square root of num
if num % i == 0:
return False # Found a factor, so not prime
return True # No factors were found, it's prime

# Get number from user
user_input = int(input("Enter a number to check if it is prime: "))
if is_prime(user_input):
print(f"{user_input} is a prime number.")
else:
print(f"{user_input} is not a prime number.")