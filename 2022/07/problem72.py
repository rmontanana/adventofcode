"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
"""


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name, father=None, size=0):
        self.name = name
        self.size = size
        self.separator = "/"
        self.children = []
        self.father = father

    def add_child(self, obj):
        self.children.append(obj)

    def get_father(self):
        if self.father:
            return self.father
        raise ValueError(f"{self.name} has No parent")

    def get_folder(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError(f"{name} not found in {self.name}")

    def print_folder(self, tail="", level=0):
        folder_name = f"{tail:{level*2}s}{self.separator}{self.name}"
        print(f"{folder_name} => {self.size:10,d}")
        for child in self.children:
            if isinstance(child, Folder):
                child.print_folder(
                    tail=tail + self.separator + self.name, level=level + 1
                )
            else:
                print(
                    f"{folder_name}{self.separator}{child.name:15s} -> {child.size:7,d}"
                )

    def size_less_than(self, value):
        if self.size < value:
            pila = [self.size]
        else:
            pila = []
        for child in self.children:
            if isinstance(child, Folder):
                pila.extend(child.size_less_than(value))
        return pila

    def size_greater_than_equal(self, value):
        if self.size >= value:
            pila = [self.size]
        else:
            pila = []
        for child in self.children:
            if isinstance(child, Folder):
                pila.extend(child.size_greater_than_equal(value))
        return pila

    def compute_sizes(self):
        for child in self.children:
            if isinstance(child, Folder):
                child.compute_sizes()
                self.size += child.size
            else:
                self.size += child.size


with open("input.txt") as f:
    lines = f.read().splitlines()
separator = "/"
root = Folder("root", father=None)
current_dir = root
idx = 0
while idx < len(lines):
    prompt, command = lines[idx].split(" ", 1)
    if prompt != "$":
        raise ValueError(f"Invalid prompt: {prompt}")
    match command.split():
        case ["cd", name]:
            match name:
                case "..":
                    current_dir = current_dir.get_father()
                case "/":
                    current_dir = root
                case _:
                    current_dir = current_dir.get_folder(name)
            idx += 1
        case ("ls",):
            idx += 1
            while idx < len(lines) and not lines[idx].startswith("$"):
                item, name = lines[idx].split(" ")
                if item == "dir":
                    current_dir.add_child(Folder(name=name, father=current_dir))
                else:
                    current_dir.add_child(File(name=name, size=int(item)))
                idx += 1
        case _:
            raise ValueError(f"Unknown command: {command}")

root.compute_sizes()
root.print_folder()
removing = root.size - 4e7
print("Removing", removing)
print(min(root.size_greater_than_equal(removing)))
