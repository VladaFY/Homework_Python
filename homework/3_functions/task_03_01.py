phonebook = {}

def add_entry():
    """Add a new entry to the phonebook."""
    name = input("Enter name: ")
    number = input("Enter number: ")
    if name in phonebook:
        phonebook[name].append(number)
    else:
        phonebook[name] = [number]

def display_numbers():
    """Display all numbers for a given name."""
    name = input("Enter name: ")
    if name in phonebook:
        print(f"имя         номер")
        for number in phonebook[name]:
            print(f"{name}      {number}")
    else:
        print("No entries found for this name.")

def delete_entry():
    """Delete all entries for a given name."""
    name = input("Enter name: ")
    if name in phonebook:
        del phonebook[name]
        print("Entries deleted.")
    else:
        print("No entries found for this name.")

def menu():
    op_types = {"1": add_entry, "2": display_numbers, "3": delete_entry}
    """Display the menu and handle user choice."""
    while True:
        print("\n1. Add number")
        print("2. Display numbers")
        print("3. Delete numbers")
        choice = input("Choose an option: ")
        try: 
            op_types[choice]()
        except KeyError:
            print("Invalid choice. Please try again.")

menu()