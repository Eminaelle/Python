students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i+1, student)

students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"}
for student in students:
    print(student, students[student], sep=", " )

students = [
    {"name": "Hermione", "house":"Gryffindor","patronus":"Otter"},
    {"name": "Harry", "house":"Gryffindor","patronus":"Stag"},
    {"name": "Ron", "house":"Gryffindor","patronus":"Jack Russel terrier"},
    {"name": "Draco", "house":"Slytherin","patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")