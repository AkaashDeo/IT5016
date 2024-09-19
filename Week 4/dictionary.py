def main():
    # Dictionary to store contacts
    contacts = {"Jill": 3456, "James": 67}
    
    # Displaying the contacts
    print("Contact List:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

    # Adding a new contact
    contacts["Alice"] = 1234
    print("\nAfter adding Alice:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

    # Removing a contact
    del contacts["James"]
    print("\nAfter removing James:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

    # Checking if a contact exists
    if "Jill" in contacts:
        print("\nJill is in the contact list.")
    else:
        print("\nJill is not in the contact list.")

main()                                               # Call the main function

