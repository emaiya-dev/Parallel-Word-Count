# Sequential Word Count Application
# Counts words in multiple text files one by one
# Processes files sequentially

import time

files = [
    "data/large1.txt",
    "data/large2.txt",
    "data/large3.txt"
]

start_time = time.perf_counter()

total_words = 0
results = []

#for filename in files:
#    with open(filename, "r", encoding="utf-8") as file:
#        text = file.read()

for filename in files:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            
 #   except FileNotFoundError:
 #       print("Error: Input file not found:", filename)
 #       break        

    except FileNotFoundError:
        print("Error: Input file not found:", filename)
        raise SystemExit(1)

    words = text.split()
    word_count = len(words)

    results.append((filename, word_count))
    total_words += word_count

end_time = time.perf_counter()

for filename, word_count in results:
    print(filename, ":", word_count)

print("Total words:", total_words)
print("Execution time:", end_time - start_time, "seconds")

