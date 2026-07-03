# Student

# Name = Bhavesh
# Age = 21
# College = RAIT
# City = Mumbai
# CGPA = 7.5


student = {
    "Name": "Bhavesh",  
    "Age": 21,
    "College": "RAIT",          
    "City": "Mumbai",
    "CGPA": 7.5
}
# print(student["Name"])
# print(student["CGPA"])
# # how to change the value of a key in a dictionary
# student["City"] = "navi mumbai"
# student["skill"] = "Python"
# print(student)

pop_value = student.pop("CGPA")
print(student)

print(student.get("Name"))

print(student.keys())