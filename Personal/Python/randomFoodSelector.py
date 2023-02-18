import random

# List of different type of foods
num = 1
foodType = []
numFood = int(input("Please list how many places/food you can't pick from: "))

print("\nThis program will pick a restaurant or food at random since your indecisive ass can't decide")

# Gets the restaurant or type of food the user can't choose from
for i in range(numFood):
    listFood = (input(f"\nRestaurant/Food #{num}: "))
    foodType.append(listFood)
    num += 1

# Prints out what the user is going to eat
randomChooser = random.choices(foodType, k=1)
print(f"\nThe restraunt/type of food you ARE going to eat is {randomChooser}. Enjoy :D")
