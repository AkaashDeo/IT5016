"""
Lab 3 - Decision Based on Total
Create a Python function to categorize and provide a recommendation based on the total amount.

Instructions:
1. Define a Function:
- Name the function `categorize_request`

2. Categorize Based on Total:
- If the total amount is less than $150, set the category to "Low".
- If the total amount is $150 or more, assign the category to "High".

3. Generate Recommendation:
- Based on the category:
    - Low: Recommend “Proceed with standard processing.”
    - High: Recommend “Review for potential discounts.”

4. Display Category and Recommendation:
- Print the determined category and the corresponding recommendation.

Author: Akaash Deo
"""

def categorize_request(total_amount):
    # Categorize based on the total amount
    if total_amount < 150:
        category = "Low"                                      # Assign category for low total
        recommendation = "Proceed with standard processing."  # Recommendation for low category
    else:
        category = "High"                                     # Assign category for high total
        recommendation = "Review for potential discounts."    # Recommendation for high category
    
    # Output the category and recommendation
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

# Example
total_amount_example = 120                                    # Replace with any total amount to test
categorize_request(total_amount_example)
