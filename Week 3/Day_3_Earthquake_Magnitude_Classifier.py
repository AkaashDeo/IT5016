def magnitude():
    """
    Function to classify earthquake magnitudes.
    Author: Rajiv Deo
    """

    message = "The Earthquake is"                              # Message to display with the magnitude classification
    user_entry = float(input("Enter earthquake magnitude: "))  # User input for earthquake magnitude

    """Classify the magnitude based on predefined ranges"""
    if user_entry < 2.0:
        print(message, "micro")                                # Classification for magnitudes less than 2.0
    elif user_entry >= 2.0 and user_entry < 3.0:
        print(message, "Very Minor")                           # Classification for magnitudes between 2.0 and 3.0
    elif user_entry >= 3.0 and user_entry < 4.0:
        print(message, "Minor")                                # Classification for magnitudes between 3.0 and 4.0
    elif user_entry >= 4.0 and user_entry < 5.0:
        print(message, "Light")                                # Classification for magnitudes between 4.0 and 5.0
    elif user_entry >= 5.0 and user_entry < 6.0:
        print(message, "Moderate")                             # Classification for magnitudes between 5.0 and 6.0
    elif user_entry >= 6.0 and user_entry < 7.0:
        print(message, "Strong")                               # Classification for magnitudes between 6.0 and 7.0
    elif user_entry >= 7.0 and user_entry < 8.0:
        print(message, "Major")                                # Classification for magnitudes between 7.0 and 8.0
    elif user_entry >= 8.0 and user_entry < 10.0:
        print(message, "Great")                                # Classification for magnitudes between 8.0 and 10.0
    elif user_entry > 10.0: 
        print(message, "Meteoric")                             # Classification for magnitudes greater than 10.0
    else:
        print("")                                              # Print an empty line for unhandled cases
 
magnitude()                                                    # Call the magnitude function to execute

