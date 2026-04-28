import sqlite3

#Database and table
def setup_database():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        issue TEXT,
        priority TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_ticket():
    name = input("Enter your name: ")
    issue = input("Enter issue: ")
    priority = input("Enter priority (Low/Medium/High): ")

    # Validation 
    if name == "" or issue == "":
        print("Error: Fields cannot be empty\n")
        return

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tickets (name, issue, priority, status) VALUES (?, ?, ?, ?)",
        (name, issue, priority, "Open")
    )

    conn.commit()
    conn.close()

    print("Ticket added successfully!\n")


# View tickets
def view_tickets():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    rows = cursor.fetchall()

    conn.close()

    if len(rows) == 0:
        print("No tickets found.\n")
    else:
        print("*** Tickets ***")

    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Issue:", row[2])
        print("Priority:", row[3])
        print("Status:", row[4])

    print()

def update_ticket_status():
    print("Update Ticket Status")

    ticket_id = input("Enter Ticket ID: ")
    new_status = input("Enter new status (Open / In Progress / Resolved): ")

    conn = sqlite3.connect("school_helpdesk.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tickets SET status = ? WHERE id = ?",
        (new_status, ticket_id)
    )

    conn.commit()
    conn.close()

    print("Ticket status updated successfully!\n")


# Main menu
def main():
    setup_database()

    while True:
        print("Help Desk System")
        print("1. Add Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket_status()
        elif choice == "4":
            print("Exiting system.")
            break


# Run program
if __name__ == "__main__":
    main()