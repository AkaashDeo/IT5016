def wavelength_colour():
    """
    Converts a wavelength in nanometers to its corresponding color.
    Author: Rajiv Deo
    """

    prompt = "Welcome to Wavelength to Colour Converter. Please enter an integer wavelength between 380 and 750 nanometers: "
    user_entry = int(input(prompt)) # Get user input for wavelength
    print(user_entry)

    # Determine color based on the wavelength range
    if 620 < user_entry <= 750:
        print(f"{prompt} Thank you, the wavelength that you entered in nanometers is {user_entry}. The colour for this wavelength is Red")
    elif 590 <= user_entry < 620:
        print(f"{prompt} Thank you, the wavelength that you entered in nanometers is {user_entry}. The colour for this wavelength is Orange")
    elif 570 <= user_entry < 590:
        print(f"{prompt} Thank you, the wavelength that you entered in nanometers is {user_entry}. The colour for this wavelength is Yellow")  
    elif 495 <= user_entry < 570:
        print(f"{prompt} Thank you, the wavelength that you entered in nanometers is {user_entry}. The colour for this wavelength is Green")
    elif 450 <= user_entry < 495:
        print(f"{prompt} Thank you, the wavelength that you entered in nanometers is {user_entry}. The colour for this wavelength is Blue")  
    elif 380 <= user_entry < 450:
        print(f"{prompt} Thank you, the wavelength that you entered in nanometers is {user_entry}. The colour for this wavelength is Violet")    
    else:
        print("Incorrect selection")  # Handle out-of-range input

# Execute the wavelength_colour function
wavelength_colour()

# Lecturer's answer

def wavelength_to_color(wave_length):
    """
    Converts a wavelength in nanometers to its corresponding color.
    Parameters:
        wave_length (int): The wavelength in nanometers.
    Returns:
        str: The color corresponding to the wavelength.
    """
    if wave_length > 750:
        return "The wavelength entered is higher than the visible spectrum! This is infrared."
    elif wave_length >= 620:
        return "Red"
    elif wave_length >= 590:
        return "Orange"
    elif wave_length >= 570:
        return "Yellow"
    elif wave_length >= 495:
        return "Green"
    elif wave_length >= 450:
        return "Blue"
    elif wave_length >= 380:
        return "Violet"
    else:
        return "Indeterminate, :-(, the number entered is outside the visible spectrum!"

# Main execution
print("Welcome to Wavelength to Colour Converter\n")
wave_length = int(input("Please enter an integer wavelength between 380 and 750 nanometers: "))
print(f"Thank you, the wavelength that you entered in nanometers is: {wave_length}\n")
print(f"The colour for this wavelength is... {wavelength_to_color(wave_length)}\n")
