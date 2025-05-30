class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.full_name = name
        self.job_title = position

    def __repr__(self):
        return f"Employee(id={self.emp_id}, name='{self.full_name}', position='{self.job_title}')"


class BTreeNode:
    def __init__(self, degree, is_leaf=False):
        self.degree = degree
        self.is_leaf = is_leaf
        self.entries = []
        self.children = []

    def traverse(self):
        for i in range(len(self.entries)):
            if not self.is_leaf:
                self.children[i].traverse()
            print(self.entries[i][1])
        if not self.is_leaf:
            self.children[-1].traverse()

    def search(self, key):
        idx = 0
        while idx < len(self.entries) and key > self.entries[idx][0]:
            idx += 1
        if idx < len(self.entries) and self.entries[idx][0] == key:
            return self.entries[idx][1]
        if self.is_leaf:
            return None
        return self.children[idx].search(key)

    def insert_non_full(self, key, employee):
        idx = len(self.entries) - 1
        if self.is_leaf:
            self.entries.append((None, None))
            while idx >= 0 and key < self.entries[idx][0]:
                self.entries[idx + 1] = self.entries[idx]
                idx -= 1
            self.entries[idx + 1] = (key, employee)
        else:
            while idx >= 0 and key < self.entries[idx][0]:
                idx -= 1
            idx += 1
            if len(self.children[idx].entries) == 2 * self.degree - 1:
                self.split_child(idx)
                if key > self.entries[idx][0]:
                    idx += 1
            self.children[idx].insert_non_full(key, employee)

    def split_child(self, idx):
        d = self.degree
        y = self.children[idx]
        z = BTreeNode(d, y.is_leaf)
        z.entries = y.entries[d:]
        y.entries = y.entries[:d - 1]
        if not y.is_leaf:
            z.children = y.children[d:]
            y.children = y.children[:d]
        self.children.insert(idx + 1, z)
        self.entries.insert(idx, y.entries.pop(-1))


class BTree:
    def __init__(self, degree):
        self.degree = degree
        self.root = BTreeNode(degree, True)

    def insert(self, key, employee):
        root = self.root
        if len(root.entries) == 2 * self.degree - 1:
            new_root = BTreeNode(self.degree, False)
            new_root.children.insert(0, self.root)
            new_root.split_child(0)
            idx = 0
            if new_root.entries[0][0] < key:
                idx += 1
            new_root.children[idx].insert_non_full(key, employee)
            self.root = new_root
        else:
            root.insert_non_full(key, employee)

    def search(self, key):
        return self.root.search(key)

    def traverse(self):
        self.root.traverse()


btree_by_emp_id = BTree(degree=3)
btree_by_emp_name = BTree(degree=3)

def add_employee():
    try:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        employee = Employee(emp_id, name, position)
        btree_by_emp_id.insert(emp_id, employee)
        btree_by_emp_name.insert(name, employee)
        print("Employee added successfully.\n")
    except ValueError:
        print("Invalid ID.\n")

def search_by_id():
    try:
        emp_id = int(input("Enter ID to search: "))
        result = btree_by_emp_id.search(emp_id)
        if result:
            print("Result found:", result)
        else:
            print("No employee found with this ID.\n")
    except ValueError:
        print("Invalid ID.\n")

def search_by_name():
    name = input("Enter name to search: ")
    result = btree_by_emp_name.search(name)
    if result:
        print("Result found:", result)
    else:
        print("No employee found with this name.\n")

def show_all():
    print("\nList of employees (by ID order):")
    btree_by_emp_id.traverse()
    print()

def menu():
    while True:
        print("""
Menu:
1. Add employee
2. Search by ID
3. Search by name
4. Show all employees
5. Exit
        """)
        user_choice = input("Choice: ")
        if user_choice == '1':
            add_employee()
        elif user_choice == '2':
            search_by_id()
        elif user_choice == '3':
            search_by_name()
        elif user_choice == '4':
            show_all()
        elif user_choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == '__main__':
    menu()