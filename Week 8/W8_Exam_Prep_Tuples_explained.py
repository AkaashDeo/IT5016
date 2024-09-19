
"""

Tuples: In Python, a tuple is an immutable sequence type, meaning once it's created, its contents cannot be changed.

Explanation of Tuples in This Code

Immutable Sequence: The students tuple is an immutable sequence of student records. 
Tuples are used here because the data does not need to be changed once defined.

Accessing Elements: Each students record is a tuple, and you access elements by indexing (e.g., record[2] for the grade).

Tuple of Tuples: The students tuple contains other tuples, each representing a student. This nested structure is useful for
 organizing and grouping related data.

Output
When you run the main function, it will calculate and print the average grade of the students.

Summary
Tuples: In this code, tuples are used to store and organize student records in an immutable and structured format.

Usage: The average_grade function processes this tuple of tuples to compute the average grade by
 extracting and summing specific elements (grades) from the nested tuples.

Benefits: Using tuples helps keep the data organized and ensures that the records remain unchanged throughout the program.

Author: Akaash Deo
"""

# Function Definition
def average_grade(records):    # Parameter: records is expected to be a list or tuple of tuples (similar to the students tuple).
    total_grade = sum(record[2] for record in records) # This is a generator expression that iterates through each tuple (record) in records and extracts the third element (record[2]), which is the grade. The sum function then adds these grades together.
    return total_grade / len(records)    # This function returns the average grade, calculated by dividing the total grade by the number of records.

students = ( 
    ('James', 20, 85),  # Each inner tuple represents a record for a student with the values: name, age, and grade.
    ('Sumeet', 22, 90),
    ('Modi', 20, 95)
)

# Function Definition: main
def main():
    avg_grade = average_grade(students) # Calling average_grade: The main function calls average_grade, passing the students tuple as the argument.
    print("Average Grade:", avg_grade)   # It prints the average grade calculated by the average_grade function.

main()  # This line calls the main function to execute the program.
