# Test Empty File and Missing File Handling

# Test 1: Empty File
print("TEST 1: Empty File")

try:
    with open("data/empty.txt", "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    word_count = len(words)

    print("Words in empty file:", word_count)

    if word_count == 0:
        print("PASS: Empty file returns 0 words.")
    else:
        print("FAIL: Empty file should return 0 words.")

except FileNotFoundError:
    print("FAIL: Empty file was not found.")


print("\n-----------------------------")


# Test 2: Missing File
print("TEST 2: Missing File")

try:
    with open("data/missing.txt", "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    print("Words in missing file:", len(words))

except FileNotFoundError:
    print("PASS: Missing file error handled correctly.")
