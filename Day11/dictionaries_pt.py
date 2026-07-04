# Write a small program that does all four:

# student = {
#     "name": "Bhavesh",
#     "age": 21
# }
# Print all key-value pairs using items().
# Use update() to add:
# "cgpa": 7.5
# "city": "Mumbai"

# Create:

# student2 = student.copy()

# Change only:

# student2["name"] = "Rahul"
# Print both dictionaries.

student = {
    "name": "Bhavesh",
    "age": 21
}

for key, value in student.items():
    print(f"{key}: {value}")

student.update({"cgpa": 7.5, "city": "Mumbai"})
student2 = student.copy()
student2["name"] = "Rahul"
print(student)
print(student2)