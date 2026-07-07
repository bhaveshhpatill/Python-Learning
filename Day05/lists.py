# -----------------------------
# Day 5 - Lists Practice
# Topic: Lists, append(), pop(), len(), for loops
# -----------------------------

# =============================
# Example 1 - Accessing elements
# =============================

languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]

print("First language:", languages[0])
print("Last language:", languages[-1])


# =============================
# Example 2 - Creating an empty list
# =============================

languages = []

languages.append("Linux")
languages.append("Python")
languages.append("C++")
languages.append("Java")

print("\nLanguages:", languages)


# =============================
# Example 3 - Length of a list
# =============================

languages = ["Python", "Java", "C++"]

print("\nNumber of languages:", len(languages))


# =============================
# Example 4 - pop()
# =============================

languages = ["Python", "Java", "C++", "JavaScript", "Java"]

removed_language = languages.pop(4)

print("\nRemoved:", removed_language)
print("Updated list:", languages)


