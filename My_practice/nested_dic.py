
# Nested Dictionary – Find Total Marks
#
# Question:
# Calculate total marks of each student.

students = {
    "Alice": {"Math": 80, "Science": 90, "English": 85},
    "Bob": {"Math": 70, "Science": 75, "English": 80}
}
for k,v in students.items():
    total=sum(v.values())
    print(f"{total}")