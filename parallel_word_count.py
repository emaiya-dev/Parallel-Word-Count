# Parallel Word Count Application
# Counts words in multiple text files using worker processes
# Multiprocessing with three worker processes

import os
import time
from concurrent.futures import ProcessPoolExecutor




def count_file_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()

        return filename, len(words), os.getpid()

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {filename}")


files = [
    "data/large1.txt",
    "data/large2.txt",
    "data/large3.txt"
]





if __name__ == "__main__":
    start_time = time.perf_counter()

    try:
        with ProcessPoolExecutor(max_workers=3) as executor:
            results = list(executor.map(count_file_words, files))

    except FileNotFoundError as error:
        print("Error:", error)
        raise SystemExit(1)

#    with ProcessPoolExecutor(max_workers=3) as executor:
#        results = list(executor.map(count_file_words, files))

    end_time = time.perf_counter()

    total_words = 0

    for filename, word_count, process_id in results:
        print(filename, ":", word_count, "| Process:", process_id)
        total_words += word_count

    print("Total words:", total_words)
    print("Execution time for pwc:", end_time - start_time, "seconds")
