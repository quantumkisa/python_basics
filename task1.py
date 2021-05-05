import os


def scan_folder(parent):
    for file_name in os.listdir(parent):
        current_path = "".join((parent, "/", file_name))
        if file_name.endswith(".txt"):
            with open(current_path, 'r') as f:
                print(f.read())
        else:
            if os.path.isdir(current_path):
                scan_folder(current_path)

scan_folder('/Users/quantumkisa/Documents/My Documents/файлы/тест/data')
