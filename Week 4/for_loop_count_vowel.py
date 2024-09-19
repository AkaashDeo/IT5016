"""
'for' loop that counts the number of vowels in given text.

Author: Akaash Deo
"""

def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text:
        if char.lower() in vowels:                        # Convert to lower case to simplify the comparison
            count += 1
    return count

def main():
    text = input("Enter the text: ")
    vowel_count = count_vowels(text)
    print(f"Number of vowels in '{text}': {vowel_count}")

main()                                                    # Call the main function

