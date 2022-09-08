hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

tott = hour*60 + mins + dura
toth = int(round(tott/60, 0))
totm = int(round(tott-toth*60, 0))

# End time = 

print("\nYour event starts at", str(hour) + ":" + str(mins), "and will take aprox.", dura, "minutes...\n")
print("It will be finished at", str(toth) + ":" + str(totm))