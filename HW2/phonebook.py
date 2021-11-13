# Robert Kwaśny



class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def addNumber(self, name, number):
        if name in self.phonebook:
            self.phonebook[name].append(number)
        else:
            self.phonebook[name] = [number]

    def getNumber(self, name):
        return self.phonebook[name]

    # Deleting the only number of a person removes the entire person
    def deleteNumber(self, name, number):
        if len(self.phonebook[name]) > 1:
            self.phonebook[name].remove(number)
        else:
            self.phonebook.pop(name, None)

    def printPhonebook(self):
        for name in self.phonebook:
            if len(self.phonebook[name]) == 1:
                print(f"{name}: ", self.phonebook[name][0])
            else:
                numbers = ", ".join(self.phonebook[name])
                print(f"{name}:", numbers)


def test():

    # Create an empty phonebook
    test_phonebook = PhoneBook()

    # Add a new person with a new number
    test_phonebook.addNumber("Ala Wesołowska", "+048 513 056 121")
    test_phonebook.addNumber("John Smith", "469-452-199")

    # Insert a second number for a given person
    test_phonebook.addNumber("Ala Wesołowska", "+048 123 456 789")

    # Retrieve number(s) of the indicated person
    test_phonebook.getNumber("Ala Wesołowska")
    test_phonebook.getNumber("John Smith")

    # Print phonebook
    test_phonebook.printPhonebook()

    # Delete numbers
    test_phonebook.deleteNumber("Ala Wesołowska", "+048 123 456 789")
    test_phonebook.deleteNumber("John Smith", "469-452-199")


if __name__ == "__main__":
    test()
