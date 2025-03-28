feet_inches = input("Enter feet and inches: ")

def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    return feet * 0.3048 + inches * 0.0254

f, i = parse(feet_inches)
result = convert(f, i)

if result < 1:
    print("Too small")
else:
    print("Big enough")