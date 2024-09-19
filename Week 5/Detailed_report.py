"""
Lab 4 - Detailed Report
Create a function to produce a detailed report based on user data and categorization from previous labs.

Instructions:
1. Define a Function: Name the function `create_detailed_report`.
2. Display Report Information:
    • User's Name
    • Total Amount
    • Category
    • Recommendation
3. Format the Output: Ensure the report is well-organized and clear.

Author: Akaash Deo
"""

def create_detailed_report(name, total_amount, category, recommendation, unique_id):
    # Display the detailed report
    print("Detailed Report:")
    print(f"Unique ID: {unique_id}")                       # User's unique identifier
    print(f"Username: {name}")                             # User's name
    print(f"Total Amount: ${total_amount:.2f}")            # Total amount formatted to two decimal places
    print(f"Category: {category}")                         # Categorization based on the total amount
    print(f"Recommendation: {recommendation}")             # Recommendation based on the category

# Example 
name_example = "Alice"                                     # Replace with the user's name
total_amount_example = 120.50                              # Replace with the total amount
category_example = "Low"                                   # Replace with the determined category
recommendation_example = "Proceed with standard processing."  # Replace with the recommendation
unique_id_example = 5001                                   # Replace with the user's unique ID

create_detailed_report(name_example, total_amount_example, category_example, recommendation_example, unique_id_example)
