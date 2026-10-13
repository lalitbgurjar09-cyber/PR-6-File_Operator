#project-6 : file operator
import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        text = input("Enter your journal entry:\n").strip()
        if text == "":
            print("Entry cannot be empty.")
            return

        try:
            try:
                with open(self.filename, "x"):
                    pass
            except FileExistsError:
                pass

            stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.filename, "a") as f:
                f.write(f"[{stamp}]\n{text}\n\n")

            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: You do not have permission to write to the journal file.")
        except OSError as e:
            print("Error: Could not write to the file.", e)

    def _read_entries(self):

        with open(self.filename, "r") as f:
            content = f.read()
        return [block for block in content.split("\n\n") if block.strip()]

    def view_entries(self):
        try:
            entries = self._read_entries()
        except FileNotFoundError:
            print("Error: The journal file does not exist. Please add a new entry first.")
            return
        except PermissionError:
            print("Error: You do not have permission to read the journal file.")
            return
        except OSError as e:
            print("Error: Could not read the file.", e)
            return

        if not entries:
            print("No journal entries found. Start by adding a new entry!")
            return

        print("Your Journal Entries:")
        print("-" * 34)
        for entry in entries:
            print(entry)
            print()

    def search_entries(self):
        keyword = input("Enter a keyword or date to search: ").strip()
        if keyword == "":
            print("Search cannot be empty.")
            return

        try:
            entries = self._read_entries()
        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
            return
        except PermissionError:
            print("Error: You do not have permission to read the journal file.")
            return
        except OSError as e:
            print("Error: Could not read the file.", e)
            return
        matches = [e for e in entries if keyword.lower() in e.lower()]

        if matches:
            print("\nMatching Entries:")
            print("-" * 34)
            for entry in matches:
                print(entry)
                print()
        else:
            print(f"\nNo entries were found for the keyword: {keyword}.")

    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        answer = input("Are you sure you want to delete all entries? (yes/no): ")
        if answer.strip().lower() != "yes":
            print("Delete cancelled.")
            return

        try:
            os.remove(self.filename)
            print("All journal entries have been deleted.")
        except PermissionError:
            print("Error: You do not have permission to delete the journal file.")
        except FileNotFoundError:
            print("No journal entries to delete.")
        except OSError as e:
            print("Error: Could not delete the file.", e)

    def show_menu(self):
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("\nUser Input: ").strip()
            print()

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_entries()
            elif choice == "3":
                self.search_entries()
            elif choice == "4":
                self.delete_entries()
            elif choice == "5":
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    try:
        JournalManager().run()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed. Goodbye!")
