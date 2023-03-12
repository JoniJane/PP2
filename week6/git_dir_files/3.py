import os
path = input()  

if os.path.exists(path):
    print("directory :", os.path.dirname(path))
    print("file name :", os.path.basename(path))
else:
    print("The path does not exist")