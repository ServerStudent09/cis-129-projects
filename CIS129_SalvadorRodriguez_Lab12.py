"""
Class Pet Program
Created By: Salvador Rodriguez
Date: 28 April 2025
Description: The purpose of this program is to create a class pet that has a name,
says what type of animal it is, and how old the pet is.
"""

class Pet:
    """Represents a pet with a name, type, and age."""

    def __init__(self, name="", pet_type="", age=0):
        """Constructor to initialize a pet."""
        self.name = name
        self.pet_type = pet_type
        self.age = age

    # Mutators (setters)
    def set_name(self, name):
        """Set the name of the pet."""
        self.name = name

    def set_type(self, pet_type):
        """Set the type of the pet."""
        self.pet_type = pet_type

    def set_age(self, age):
        """Set the age of the pet."""
        self.age = age

    # Accessors (getters)
    def get_name(self):
        """Get the name of the pet."""
        return self.name

    def get_type(self):
        """Get the type of the pet."""
        return self.pet_type

    def get_age(self):
        """Get the age of the pet."""
        return self.age


# Main function
def main():
    """Collect pet information and display it."""
    # Create a Pet object
    animal = Pet()

    # Get values for the pet
    input_name = input("Enter a pet name: ")
    animal.set_name(input_name)

    input_type = input("Enter a pet type: ")
    animal.set_type(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.set_age(input_age)

    # Show values for this pet
    print("\nThe pet name is:", animal.get_name())
    print("The pet type is:", animal.get_type())
    print("The pet age is:", animal.get_age())


# Run the main function
if __name__ == "__main__":
    main()
