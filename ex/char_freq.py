# Char freq

st = input("Enter a string :")

freq = {}

for c in st:
    if c not in freq:
        freq[c] = st.count(c)

print(freq)


