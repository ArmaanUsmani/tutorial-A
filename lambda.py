people = [
    {"name": "Armaan", "house": "Antilia"},
    {"name": "Sameer", "house": "Mannat"}
]
people.sort(key=lambda person: person["name"])

print(people)