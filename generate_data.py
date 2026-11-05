# Test Data Generator
# Creates large text files for word-count performance testing

sentence = "Python parallel processing can improve performance when tasks are divided among multiple workers. "

files = [
        "data/large1.txt",
        "data/large2.txt",
        "data/large3.txt",
    ]

for filename in files:
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(1000000):
            file.write(sentence)

print("LARGE test files created successfully.")
