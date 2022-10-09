# Assignment 1: Text Processing with Python
# This program:
#   - reads in an input file (data/data.csv) that contains employee information
#   - processes the text to a more standardized format
#   - creates an object for each person with format corrections from the user
#   - displays the updated information of each person

import sys, os, csv, re, pickle

# if sysarg does not include relative path of input file, prints error message and ends program
if len(sys.argv) < 2:
        print("Please enter the relative path of the input file as a system arg")
        exit(1)

# Person class for employee data from input file fields (last, first, mi, id, phone)
class Person:
    # constructor method that initializes object attributes
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # method that outputs fields for each employee from input file
    def display(self):
        print("Employee ID: ", self.id)
        print("\t     ", self.first, self.mi, self.last)
        print("\t     ", self.phone, "\n")

# main function
def main():
    # sets dictionary for employees from input file
    persons = {}
    persons = process_text(persons)

    # saves dictionary as pickle file using write binary
    pickle.dump(persons, open('persons.p', 'wb'))
    # opens and reads pickle file using read binary
    persons_in = pickle.load(open('persons.p', 'rb'))

    # loops through dict of persons to display each person by verifying unpickling
    print("\nEmployee list:\n")
    for person in persons_in.keys():
        persons_in[person].display()

# function that processes text from input file
def process_text(persons):
    # user specifies the relative path ‘data/data.csv’ in a sysarg
    filepath = sys.argv[1]
    # opens input file for reading
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        # reads in input file text starting from second line to get rid of heading
        f.readline()
        # splits text on comma to get fields as text variables
        csv_reader = csv.reader(f)
        # loops through fields for each employee in each row
        for row in csv_reader:
            text = row

            # declares variables for each field
            last = text[0]
            first = text[1]
            mi = text[2]
            id = text[3]
            phone = text[4]

            # modifies first letter of last name and first name to be capitalized
            last = last.capitalize()
            first = first.capitalize()

            # modifies middle initial to be a single upper case letter and adds 'X' for missing middle initials
            if not mi:
                mi = "X"
            mi = mi.capitalize()

            # uses regex to validate ID format by modifying incorrect ID forms
            while re.match('[A-Za-z][A-Za-z]\d{4}', id) is None:
                print("ID invalid:", id)
                print("ID is two letters followed by 4 digits")
                id = input("Please enter a valid ID: ")
                # checks for duplicate ID and prints error message if ID already exists in input file
                while id in persons.keys():
                    print("ID", id, "already exists in file")
                    id = input("Please enter a valid ID: ")

            # modifies phone number to be in form 999-999-9999
            while re.match('\d{3}-\d{3}-\d{4}', phone) is None:
                print("Phone", phone, "is invalid")
                print("Enter phone number in form 123-456-7890")
                phone = input("Enter phone number: ")

            # creates Person object
            person = Person(last, first, mi, id, phone)
            
            # saves object to a dict of persons, where ID is the key
            persons[id] = person
            
    # returns dict of persons to main function
    return persons

# calls main function
if __name__ == '__main__':
    main()