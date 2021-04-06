while True:
    number = input("Tell me baby, what's your story (or press q): ")
    if number.isdigit():
        number = int(number)
        if number % 2: print("odd")
        else: print("even")
    else: print("NOT VALID")
    if number == "q" or "stop": break
