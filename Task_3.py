class Document:
    def __init__(self, filename, filesize, filetype):
        self.filename = filename
        self.filesize = filesize
        self.filetype = filetype

    def __str__(self):
        return f"{self.filename} ({self.filesize} KB, {self.filetype})"


class DirectoryNode:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.documents = []
        self.left_child = None
        self.right_child = None

    def insert_document(self, doc):
        self.documents.append(doc)

    def link_left(self, node):
        self.left_child = node

    def link_right(self, node):
        self.right_child = node


def locate_document_by_name(node, target_name, current_path=""):
    if node is None:
        return None

    path = f"{current_path}/{node.folder_name}"

    for doc in node.documents:
        if doc.filename == target_name:
            return {"document": doc, "path": path}

    left_result = locate_document_by_name(node.left_child, target_name, path)
    if left_result:
        return left_result

    return locate_document_by_name(node.right_child, target_name, path)


def interactive_directory_system():
    print("Interactive Binary Directory System")

    root_folder = input("Enter the name of the root directory: ")
    root_node = DirectoryNode(root_folder)

    directory_map = {root_folder: root_node}

    while True:
        print("\nOptions:")
        print("1. Add a directory")
        print("2. Add a document")
        print("3. Search for a document")
        print("4. Exit")

        user_choice = input("Your choice: ")

        if user_choice == "1":
            parent_folder = input("Enter the parent directory name: ")
            if parent_folder not in directory_map:
                print("Parent directory not found.")
                continue

            new_folder = input("Enter the new directory name: ")
            child_side = input("Left or Right child? (l/r): ")

            new_node = DirectoryNode(new_folder)
            if child_side.lower() == 'l':
                directory_map[parent_folder].link_left(new_node)
            elif child_side.lower() == 'r':
                directory_map[parent_folder].link_right(new_node)
            else:
                print("Invalid input.")
                continue

            directory_map[new_folder] = new_node
            print(f"Directory '{new_folder}' added to '{parent_folder}'.")

        elif user_choice == "2":
            dir_name = input("Enter the directory to add the document to: ")
            if dir_name not in directory_map:
                print("Directory not found.")
                continue

            doc_name = input("Enter the document name: ")
            doc_size = int(input("Enter the document size (KB): "))
            doc_type = input("Enter the document type (e.g. txt, jpg): ")

            new_doc = Document(doc_name, doc_size, doc_type)
            directory_map[dir_name].insert_document(new_doc)
            print(f"Document '{doc_name}' added to '{dir_name}'.")

        elif user_choice == "3":
            name_to_find = input("Enter the document name to search for: ")
            search_result = locate_document_by_name(root_node, name_to_find)
            if search_result:
                print(f"Document found: {search_result['document']}")
                print(f"Path: {search_result['path']}")
            else:
                print("Document not found.")

        elif user_choice == "4":
            print("Exiting the directory system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    interactive_directory_system()
