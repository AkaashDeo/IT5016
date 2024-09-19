def average_grade(records):
    """
    Calculates the average grade from a list of student records.

    Author: Akaash Deo
    """
    if not records:                                                   # Check if records is empty
        return 0                                                      # Return 0 if there are no records
    total_grade = sum(record[2] for record in records)                # Sum up the grades from the records
    return total_grade / len(records)                                 # Calculate and return the average grade

students = (
    ('James', 20, 85),                                                # Student record (name, age, grade)
    ('Sumeet', 22, 90),
    ('Modi', 20, 95)
)

def main():
    """
    Main function to execute the average grade calculation.
    It calculates and prints the average grade of the provided student records.
    """
    avg_grade = average_grade(students)                                # Call the average_grade function
    print("Average Grade:", avg_grade)                                 # Print the average grade

# Run the main function
if __name__ == "__main__":                                             # Check if the script is being run directly
    main()                                                             # Execute the main function
