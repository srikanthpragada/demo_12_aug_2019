import os

tree = os.walk(r'e:\c')
for (name, dirs, files) in tree:
    for f in files:
        if f.endswith(".c"):
            print(f)
