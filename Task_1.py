class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def type_text(self, new_text):
        self.undo_stack.append(('type', new_text))
        self.text += new_text
        self.redo_stack.clear()

    def delete_text(self, count):
        deleted = self.text[-count:]
        self.undo_stack.append(('delete', deleted))
        self.text = self.text[:-count]
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        action, data = self.undo_stack.pop()
        if action == 'type':
            self.text = self.text[:-len(data)]
            self.redo_stack.append(('type', data))
        elif action == 'delete':
            self.text += data
            self.redo_stack.append(('delete', data))

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        action, data = self.redo_stack.pop()
        if action == 'type':
            self.text += data
            self.undo_stack.append(('type', data))
        elif action == 'delete':
            self.text = self.text[:-len(data)]
            self.undo_stack.append(('delete', data))

    def show_text(self):
        print(f"\nCurrent text: '{self.text}'\n")

def menu():
    editor = TextEditor()
    while True:
        print("Menu")
        print("1. Type text")
        print("2. Delete text")
        print("3. Undo")
        print("4. Redo")
        print("5. Show current text")
        print("6. Quit")
        choice = input("Your choice: ")

        if choice == "1":
            text = input("Enter text to add: ")
            editor.type_text(text)
        elif choice == "2":
            try:
                count = int(input("Number of characters to delete: "))
                editor.delete_text(count)
            except ValueError:
                print("Invalid input.")
        elif choice == "3":
            editor.undo()
        elif choice == "4":
            editor.redo()
        elif choice == "5":
            editor.show_text()
        elif choice == "6":
            print("Exiting editor.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
