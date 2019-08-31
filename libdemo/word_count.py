fileobj = open("test.txt", "rt")

freq = {}

for line in fileobj:
    words = line.strip("\n").split(" ")
    for w in words:
        if w in freq:
            freq[w] += 1  # increment count
        else:
            freq[w] = 1

fileobj.close()

for w, cnt in sorted(freq.items(), key=lambda t: t[1], reverse=True):
    print(f"{w:10} {cnt}")
