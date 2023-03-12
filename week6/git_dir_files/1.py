import os
path = input()

print("All directories and files:", [i for i in os.listdir(path)])
print("Directories:", [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))])
print("Files:", [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))])