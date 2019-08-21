names = ['c', 'c++', 'python', 'java', 'f#', 'typescript', 'ruby']

for n in sorted(names, key=lambda s: s[-3:]):
    print(n)

