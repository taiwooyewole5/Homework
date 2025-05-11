print("Please enter the following infomation:")
print()

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")
noun = input("a singular noun: ")

if noun[0].lower() in 'aeiou':
    article = "an"
else:
    article = "a"

print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3}")
print(f"right in front of my family.")

# Extra creative sentence, I added this sentence because it's the only thing I could think of to make my assignments looks nice. The answer is an umbrella.
print(f"\nLater, I found {article} {noun} in my backpack—it was the weirdest day ever!")