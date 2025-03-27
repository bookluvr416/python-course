date = input("Enter today's date: ")
mood = input("How would you rate your mood? ")
thoughts = input("Let your thoughts flow: \n")

with open(f"journal/{date}.txt", 'w') as file:
    file.write(f"{mood} \n\n")
    file.write(thoughts)