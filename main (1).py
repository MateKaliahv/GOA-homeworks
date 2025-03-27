guess_number = 5
user_input = 0

while user_input != guess_number:
    user_input = int(input("Please enter number:"))

    if user_input == guess_number:
        print("You Won")
    else:
        print("Try again")

        guess_number = 5
user_input = 0
lives = 3

while user_input != guess_number and lives != 0:
    user_input = int(input("Please enter number:"))

    if user_input == guess_number:
        print("You Won")
    else:
        print("Try again")
    
    lives = lives - 1


    healthy_products = ["Tomato", "Apple", "Orange", "Alucha", "Cucumber"]

healthy_products.pop(0)
healthy_products.pop()

print(healthy_products)