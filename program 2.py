import sqlite3

def new_entry(Name, Phone_Number):
    cur.execute('INSERT INTO Entries (Name, Phone_number) VALUES (?, ?)',(Name,Phone_Number))
    print(f'Added: {Name} - {Phone_Number}')
def search(Name):
    cur.execute('SELECT Phone_Number FROM Entries WHERE Name =?',(Name,))
    result = cur.fetchone()
    print(f"{Name}'s phone number is {result[0]}")
def edit_entry(Name,Phone_Number):
    cur.execute('UPDATE Entries SET Phone_Number=? WHERE Name = ?',(New_Number, Name))
    print(f"{Name}'s phone number is now {New_Number}")
def delete(Name):
    cur.execute('DELETE FROM Entries WHERE Name = ?', (Name,))
    print(f'{Name} has been deleted')
def print_all():
    for row in cur.execute("select * from Entries"):
        print(row)

conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
while True:
    print("\nPhone Book Menu")
    print("1. Add an entry")
    print("2. Look up a phone number")
    print("3. Update a phone number")
    print("4. Delete an entry")
    print("5. Display all entries")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        Name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        new_entry(Name, phone_number)
    elif choice == '2':
        Name = input("Enter name: ")
        search(Name)
    elif choice == '3':
        Name = input("Enter name: ")
        New_Number = input("Enter new phone number: ")
        edit_entry(Name, New_Number)
    elif choice == '4':
        Name = input("Enter name: ")
        delete(Name)
    elif choice == '5':
        print_all()
    elif choice == '6':
        conn.commit()
        break
    else:
        print("Invalid choice. Please try again.")
#ethan collins 4/29/2025