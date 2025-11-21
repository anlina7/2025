import sqlite3

def create_db():
    """Creates the database tables if they don't exist."""
    conn = sqlite3.connect('party.db')
    c = conn.cursor()

    # Parties table
    c.execute('''
        CREATE TABLE IF NOT EXISTS parties (
            party_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    # Guests table (linked to a party)
    c.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
            party_id INTEGER NOT NULL,
            guest_name TEXT NOT NULL,
            FOREIGN KEY (party_id) REFERENCES parties(party_id)
        )
    ''')

    conn.commit()
    conn.close()


def add_party():
    """Adds a party with its name and date."""
    name = input("Enter Party Name: ")
    date = input("Enter Party Date (YYYY-MM-DD): ")

    conn = sqlite3.connect('party.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO parties (name, date) VALUES (?, ?)", (name, date))
        conn.commit()
        print(f"Party '{name}' on {date} added successfully!")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def add_guest():
    """Adds a guest linked to an existing party."""
    conn = sqlite3.connect('party.db')
    c = conn.cursor()

    # Show list of parties
    c.execute("SELECT party_id, name FROM parties")
    parties = c.fetchall()

    if not parties:
        print("No parties found. Add a party first.")
        conn.close()
        return

    print("\n--- Parties ---")
    for p in parties:
        print(f"{p[0]} - {p[1]}")

    try:
        party_id = int(input("Enter Party ID: "))
    except ValueError:
        print("Invalid ID.")
        conn.close()
        return

    guest_name = input("Enter Guest Name: ")

    try:
        c.execute("INSERT INTO guests (party_id, guest_name) VALUES (?, ?)", (party_id, guest_name))
        conn.commit()
        print(f"Guest '{guest_name}' added to party {party_id}!")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def view_parties():
    """Shows all parties."""
    conn = sqlite3.connect('party.db')
    c = conn.cursor()

    c.execute("SELECT * FROM parties")
    parties = c.fetchall()

    if not parties:
        print("No parties found.")
    else:
        print("\n--- All Parties ---")
        print(f"{'ID':<4} {'Name':<30} {'Date':<15}")
        print("-" * 50)
        for p in parties:
            print(f"{p[0]:<4} {p[1]:<30} {p[2]:<15}")

    conn.close()


# ---- MAIN PROGRAM ----

create_db()

while True:
    print("\n--- Party Manager ---")
    print("1 - Add party")
    print("2 - Add guest")
    print("3 - View all parties")
    print("4 - Exit")

    choice = input("Select action: ")

    if choice == "1":
        add_party()

    elif choice == "2":
        add_guest()

    elif choice == "3":
        view_parties()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option")