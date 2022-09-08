secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = int(input("Make your guess: "))

while guess != secret_number:
    print ("Well well, you've been bamboozled...", "\nHa ha! You're stuck in my loop!")
    guess = int(input("At least you can try again: "))
print("Well done, muggle! You are free now.")