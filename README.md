# Parallel Word Count Application
A Python application comparing sequential and parallel word counting using multiprocessing.

Objective
-The main objective is to demonstrate and compare sequential and parallel processing by measuring word-count accuracy and execution time.


## 1. Project Description

This project implements two approaches to count words in multiple large text files:

- Sequential Processing: Processes files one by one.
- Parallel Processing: Uses Python's ProcessPoolExecutor with three worker processes.

The application compares the execution time and word-count accuracy of both approaches.


## 2. Technologies Used

- Python
- concurrent.futures
- multiprocessing
- time
- os


## 3. Project Structure

```text
Parallel-Word-Count/
├── main.py
├── parallel_word_count.py
├── generate_data.py
├── test_empty.py
└── data.zip
```

## 4. Requirements
-Python 3.x
-Windows, Linux or macOS

*No additional Python packages are required.

## 5. Setup Instructions
-Download or clone this repository.
-Extract data.zip into the project directory.
-Make sure the extracted folder is named data.
-Ensure the text files are inside the data folder.

## 6. How to Run
--Run the sequential program: python main.py
--Run the parallel program: python parallel_word_count.py
--Run the empty-file and missing-file tests: python test_empty.py


## 7. Test Data
The data archive contains:
-large1.txt
-large2.txt
-large3.txt
-sample1.txt
-sample2.txt
-sample3.txt
-empty.txt
